import torch # type: ignore
import GPUtil # type: ignore

def check_gpu_usage():
    # Check GPU availability with PyTorch
    if torch.cuda.is_available():
        print("GPU is available!")
        device = torch.device("cuda")  # Use GPU
        gpu_name = torch.cuda.get_device_name()
        print("GPU Name:", gpu_name)
    else:
        print("GPU is not available, using CPU")
        device = torch.device("cpu")  # Use CPU

    # Monitor GPU utilization with GPUtil
    GPUs = GPUtil.getGPUs()
    for GPU in GPUs:
        print(f"GPU {GPU.id} Utilization: {GPU.load*100:.2f}%")

if __name__ == "__main__":
    check_gpu_usage()