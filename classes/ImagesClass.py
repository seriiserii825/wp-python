import os
from termcolor import colored
from rich import print
from libs.select import selectMultiple

class ImagesClass:
    def __init__(self):
        self.downloads_dir = os.path.expanduser('~') + "/Downloads"
        self.checkIfImagesInDownloads()
        self.replaceSpaceWithUnderscore()

    def checkIfImagesInDownloads(self):
        files = os.listdir(self.downloads_dir)
        for item in files:
            if item.endswith(".jpg") or item.endswith(".png") or item.endswith(".svg"):
                return True
        exit(colored("No images found in Downloads folder!", "red"))

    def replaceSpaceWithUnderscore(self):
        files = os.listdir(self.downloads_dir)
        for item in files:
            if item.endswith(".jpg") or item.endswith(".png") or item.endswith(".svg"):
                new_name = item.replace(" ", "_")
                new_name_path = os.path.join(self.downloads_dir, new_name)
                old_name_path = os.path.join(self.downloads_dir, item)
                os.rename(old_name_path, new_name_path)

    def getImages(self):
        images = []
        files = os.listdir(self.downloads_dir)
        for item in files:
            if item.endswith(".jpg") or item.endswith(".png") or item.endswith(".svg"):
                images.append(item)
        sorted_images = sorted(images)
        print(colored("Images in Downloads folder:", "blue"))
        return sorted_images

    def importImages(self, images):
        for image in images:
            if image.endswith(".jpg"):
                os.system(f"jpegoptim --strip-all --all-progressive -ptm 80 ~/Downloads/{image}")
                os.system("wp media import ~/Downloads/" + image + " --title=" + image)
            else:
                os.system("mogrify -format jpg ~/Downloads/" + image)
                new_image = image.replace(".png", ".jpg")
                os.system("rm ~/Downloads/" + image)
                os.system(f"jpegoptim --strip-all --all-progressive -ptm 80 ~/Downloads/{new_image}")
                os.system("wp media import ~/Downloads/" + new_image + " --title=" + new_image)

    def uploadAll(self):
        images = self.getImages()
        self.importImages(images)

    def selectImages(self):
        images = selectMultiple(self.getImages())
        self.importImages(images)
