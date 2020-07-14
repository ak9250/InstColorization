import runway
from PIL import Image
import inference_bbox
import test_fusion



@runway.setup()
def setup(opts):
    pass


@runway.command(name='generate',
                inputs={ 'image': image(description='Image to colorize'),
                        },
                outputs={ 'image': image(description='Colorized image') })
def generate(model, args):

    args['image'].save("example/foo.png")
    inference_bbox.calc_bbox()
    result_path = test_fusion.calc_colors()
    result = Image.open(result_path)
    return {
        'image': result
    }


if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=8888)