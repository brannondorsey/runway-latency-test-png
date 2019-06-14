import runway
from runway.data_types import image

@runway.command(name='latency_test', inputs={ 'image': image() }, outputs={ 'image': image() })
def latency_test(model, args):
    return { 'image': args['image'] }

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=8000)
