from utils import *
from todo import svd_compress


def main():
    img_path = 'img/vegetable_english.jpg'
    imArr = load_image(img_path)

    ks = [1, 5, 50, 150, 400, 1050, 1289]
    err = []
    for k in ks:
        print("Perform SVD for k=%d ..." % k, end='\r')
        imArr_compressed = svd_compress(imArr, K=k)
        err += [approx_error(imArr, imArr_compressed)]
        save_image(imArr_compressed, 'result_{}.jpg'.format(k))

    plt.imshow(imArr_compressed)
    plt.show()
    plot_curve(ks, err, show=True)

if __name__ == '__main__':
    main()
