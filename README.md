# Captcha_Breaking

## About
```
This project aims at extracting text from the captcha using pytesseract and opencv.
It is completed under the guidance and mentorship of Artificial Intelligence and Electronic Society(ArIES) of IIT Roorkee.
Mentor :  @GopiKishan14 (https://github.com/GopiKishan14)
```

## Dataset
```
- The dataset has been taken from kaggle website. Below is the link
  https://www.kaggle.com/fournierp/captcha-version-2-images
- I have only able to upload 6 captcha images because github doesn't allow to import such big memory.

```

## Code

##### Environment

```
The Following code is designed on Anaconda Spyder. You can also implement it on Google Colab. For any query do mail me.
```
### Code
```
**Code Description**

- extracting all the captcha images from the directory.
- passing one by one the images present in the direcory in the function get_string
- the get_string function first denoise the image convert it into gray scalee
- use pytesseract library to extract the text in the image
- returns the string object
```
<p align="left">
  <h3>Original Image</h3>
  <img width="100" height="100" src="https://github.com/shikhar2402/Captcha_Breaking/blob/master/output_samples/avoid-captcha.jpg">
</p>
<p align="left">
  <h3>Denoised Image</h3>
  <img width="100" height="100" src="https://github.com/shikhar2402/Captcha_Breaking/blob/master/output_samples/denoised.jpg">
</p>


## Result

- the console will give the text embedded in the image.
- the title of the image is also the text in the image

<p align="left">
  <h3>Image with Captcha</h3>
  <img width="200" height="180" src="https://github.com/shikhar2402/Captcha_Breaking/blob/master/output_samples/output.png">
</p>

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
