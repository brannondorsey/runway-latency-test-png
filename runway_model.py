import runway
import os, signal
from runway.data_types import image

@runway.command(name='latency_test', inputs={ 'image': image() }, outputs={ 'image': image() })
def latency_test(model, args):
    # Test a crash loop
    os.kill(os.getpid(), signal.SIGKILL)
    return { 'image': args['image'] }

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=8000)
