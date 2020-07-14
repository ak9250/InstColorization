
from PIL import Image
import inference_bbox
import test_fusion


Image.new("RGB", (1,1)).save("example/foo.png")
inference_bbox.calc_bbox()
result_path = test_fusion.calc_colors()
result = Image.open(result_path)

