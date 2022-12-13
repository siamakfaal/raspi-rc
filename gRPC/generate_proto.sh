#!/bin/bash

# This shell scrip generates related files to servos.proto

echo "Generating proto files..."
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. servos.proto

if [ $? -eq 0 ]; 
then 
    echo "Process completed successfully." 
else 
    echo "Process failed." 
fi