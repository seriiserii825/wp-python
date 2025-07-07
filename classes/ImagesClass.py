import os

from rich import print

from libs.select import selectMultiple


class ImagesClass:
    def __init__(self):
        self.downloads_dir = os.path.expanduser('~') + "/Downloads"
        self.checkIfImagesInDownloads()
        self.replaceSpaceWithUnderscore()

    def showImages(self):
        os.system('wp post list --post_type=attachment')

    def deleteImage(self):
        self.showImages()
        image_id = input('Enter the image ID you want to delete: ')
        if image_id.isdigit():
            os.system(f'wp post delete {image_id} --force')
        self.showImages()
        
    def checkIfImagesInDownloads(self):
        files = os.listdir(self.downloads_dir)
        for item in files:
            if item.endswith(".jpg") or item.endswith(".png") or item.endswith(".svg"):
                return True
        print(f"[red]No images found in Downloads folder!")
        exit()

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
        return sorted_images

    def optimizeImage(self, image):
        os.system(
            f"jpegoptim --strip-all --all-progressive -ptm 80 ~/Downloads/{image}")

    def uploadImage(self, image: str):
        os.system("wp media import ~/Downloads/" + image + " --title=" + image)

    def importImages(self, images):
        for image in images:
            if image.endswith(".jpg"):
                self.optimizeImage(image)
                self.uploadImage(image)
            elif image.endswith(".png"):
                print(f'{image}: image')
                convert_png = input('Do you want to convert png to jpg, (y/n)? ')
                if (convert_png == 'y'):
                    os.system("mogrify -format jpg ~/Downloads/" + image)
                    new_image = image.replace(".png", ".jpg")
                    os.system("rm ~/Downloads/" + image)
                    self.optimizeImage(new_image)
                    self.uploadImage(new_image)
                else:
                    self.uploadImage(image)
            else:
                self.uploadImage(image)
        self.showImages()

    def uploadAll(self):
        images = self.getImages()
        self.importImages(images)

    def selectImages(self):
        images = selectMultiple(self.getImages())
        self.importImages(images)
