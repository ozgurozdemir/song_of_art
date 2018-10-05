# Song Of Art
*Reveal the secret song lies down in paintings and convert that beauty to magnificent concertos*

## Prerequisites

All you need is Python3. The whole code was written with core Python3 libraries.

## Deployment

You can use terminal to run program. Put the image you want to convert, then enter your image name with *extension*. 

**Note:** Images with high resolution is recommended, in spite of running time. 

## Methodology

The taken image processed by a filter, so computer can understand intesity level of each pixel. Intensity level got by processing is used for defining the wavelength of image. Because this wavelength is noisy and not meaningful, the nearest wavelength of note (piano keys*) replaced with it. Finally, the output consists of composition of this notes.
<img src="https://user-images.githubusercontent.com/17692149/46501961-9c885a80-c82f-11e8-822a-d9ec25c110ce.png">
<sub>*Thanks to Tesabob2001 for the sound library of piano key's notes: https://freesound.org/people/Tesabob2001/packs/12995/ 
</sub>

## Examples

* Mona Lisa, *Leonardo Da Vinci* - https://soundcloud.com/ozgurozdemir/mona-lisa
* The School of Athens, *Raffaello Sanzio* - https://soundcloud.com/ozgurozdemir/the-school-of-athens
* The Scream, *Edvard Munch* - https://soundcloud.com/ozgurozdemir/the-scream
* The Starry Night, *Vincent van Gogh*  - https://soundcloud.com/ozgurozdemir/the-starry-night
* La Creazione di Adamo, *Michelangelo* - https://soundcloud.com/ozgurozdemir/la-creazione-di-adamo
* Guernica, *Pablo Picasso* - https://soundcloud.com/ozgurozdemir/guernica

## Future Work

* Use machine learning to reduce the running time by saving model
* Use the Music Theory to create harmony 
* Use Fourier transform (best result but less fun... :< )
* Use music to create pictures in another project

## Author

*Özgür Özdemir* - [LinkedIn](https://www.linkedin.com/in/%C3%B6zg%C3%BCr-%C3%B6zdemir-668110144/)

