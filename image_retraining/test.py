import os
import sys
cmd = "python image_retraining/label_image.py --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt --image="+sys.argv[1]
os.system(cmd)


