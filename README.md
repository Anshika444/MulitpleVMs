# Microservices on VirtualBox VMs

Two Python microservices running on separate VirtualBox VMs connected via Host-only network.  

- `service1.py` - VM1 API service  
- `service2.py` - VM2 client service  

Run VM1 first, then VM2. VM2 communicates with VM1 using the Host-only IP.
