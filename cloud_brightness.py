import pymeshlab
import sys
ms = pymeshlab.MeshSet()
ms.load_new_mesh(sys.argv[1])
ms.vertex_color_brightness_contrast_gamma(brightness = -15, contrast = 15, gamma = 1.57)
ms.save_current_mesh(sys.argv[1])