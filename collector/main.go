package main

import (
	"log"
	"net"
	"os"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/endpoints"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/kinesis"
	pb "github.com/bufferapp/buffer-metrics/collector/proto"
	"github.com/golang/protobuf/proto"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

const (
	port = ":50051"
)

var awsAccessKeyID string = os.Getenv("AWS_ACCESS_KEY_ID")
var awsSecretAccessKey string = os.Getenv("AWS_SECRET_ACCESS_KEY")
var kinesisStream string = os.Getenv("KINESIS_STREAM")
var svc *kinesis.Kinesis

func setupKinesis() {
	creds := credentials.NewStaticCredentials(awsAccessKeyID, awsSecretAccessKey, "")
	sess := session.Must(session.NewSession(&aws.Config{
		Credentials: creds,
		Region:      aws.String(endpoints.UsEast1RegionID),
	}))
	svc = kinesis.New(sess)
}

// putRecord sends the given type of metric to the stream using the type as partition key
func putRecord(metricType string, data []byte) error {
	input := &kinesis.PutRecordInput{
		Data:         data,
		PartitionKey: aws.String(metricType),
		StreamName:   aws.String(kinesisStream),
	}

	_, err := svc.PutRecord(input)
	if err != nil {
		log.Printf("ERROR: failed to put record: %v", err)
		return err
	}
	return nil
}

func sendMetric(metricType string, data []byte) (*pb.Response, error) {
	err := putRecord("Visit", data)
	if err != nil {
		return nil, err
	}
	return &pb.Response{Message: "Successlly recieved " + metricType}, nil
}

// Server is used to implement BufferMetricsServer
type server struct{}

// TrackVisit implements BufferMetrics.TrackVisit
func (s *server) TrackVisit(ctx context.Context, visit *pb.Visit) (*pb.Response, error) {
	data, err := proto.Marshal(visit)
	if err != nil {
		return nil, err
	}
	return sendMetric("Visit", data)
}

func main() {
	log.Println("Collector starting up")

	setupKinesis()

	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterMetricsCollectorServer(s, &server{})
	// Register reflection service on gRPC server.
	reflection.Register(s)

	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
