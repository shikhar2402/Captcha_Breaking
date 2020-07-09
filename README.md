# Captcha_Breaking

## Dataset
```
- The dataset has been taken from kaggle website. Below is the link
  https://www.kaggle.com/fournierp/captcha-version-2-images
- I have only able to upload 6 captcha images because github doesn't allow to import such big memory.

```

## Code

```
The Following code is designed on Anaconda Spyder. You can also implement it on Google Colab. For any query do mail me.

**Code Description**

- extracting all the captcha images from the directory.
- passing one by one the images present in the direcory in the function get_string
- the get_string function first denoise the image convert it into gray scalee
- use pytesseract library to extract the text in the image
- returns the string object
```

## Result

- the console will give the text embedded in the image.
- the title of the image is also the text in the image


### Setup

- You only need the following packages for runing this code

> update and install this package first

```shell
To install this package with conda run one of the following:
conda install -c conda-forge pytesseract
conda install -c conda-forge/label/cf202003 pytesseract
```

> now install openCv 

```shell
To install this package with conda run one of the following:
conda install -c conda-forge opencv
conda install -c conda-forge/label/gcc7 opencv
conda install -c conda-forge/label/broken opencv
conda install -c conda-forge/label/cf201901 opencv
conda install -c conda-forge/label/cf202003 opencv

```



---

## Support

Reach out to me at one of the following places!

- Gmail :  ssaxena@ch.iitr.ac.in
- LinkedIn :  Shikhar Saxena

---

## License
[MIT](https://choosealicense.com/licenses/mit/)
