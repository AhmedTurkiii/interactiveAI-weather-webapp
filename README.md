
<a name="readme-top"></a>




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aleguzmancs9/Weather">
    <img src="https://i.imgur.com/ZPGsx9L.png" alt="Logo" width="400" height="400">
  </a>

<h3 align="center">OtterWeather</h3>

  <p align="center">
Weather updates for otters
    <br />
    <a href="https://github.com/aleguzmancs9/Weather.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is a  weather app that uses multimedia to represent the current weather conditions.

The user will be given two options 
1. To attain the weather conditions for the current location 
2. Search for weather conditions of a desired location.

Once an option is selected the user will be brought to the results page where a background image, that matches the current weather condition, will appear. Music matching the current description will atomically play. 
The user will have the option to pause and play the music as desired. 

The weather conditions (Weather Description, Current Temperature, Wind Speed, Feels Like, & Moon Phase) will be displayed along with clothing recommendations for the current weather conditions. 

The user will also have the option to return to the home page by clicking a home page button.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Python][Python-url]
* [Flask][Flask-url]
* [OpenAI][OpenAI-url]
* [WeatherAPI][WeatherAPI-url]
* [IpstackAPI][WeatherAPI-url]
* [JavaScript][JavaScript-url]
* HTML
* CSS

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* pip
  ```sh
  python3 -m pip install –upgrade pip
  ```
* requests
  ```sh
  pip install requests
  ```
* Flask
  ```sh
  pip install flask
  ```
* matplotlib
  ```sh
  pip install matplotlib
  ```
* OpenAI
  ```sh
  pip install --upgrade openai
  ```

### Installation

1. Get a free API Key at [https://www.weatherapi.com](https://www.weatherapi.com)
2. Get a free API Key at [https://openai.com/product](https://openai.com/product)
3. Get a free API Key at [https://ipstack.com](https://ipstack.com/)

4. Import packages
   ```sh
   from flask import Flask, render_template, request, send_file
   ```
   ```sh
   from openai import OpenAI
   ```
5. Enter your API in `terminal`
   ```bash
   export OPENAI_API_KEY='Enter Your Api'
   ```
6. Enter your API in `api_key_openai`
7. Enter your API in `api_key_weatherAPI`
8. Enter your API in `api_key_ipstackAPI`

   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<div style="display: flex;">
  <img src="https://i.imgur.com/hvuodIX.png" alt="Home Page" width="300" height= "200" style="margin-right: 20px;" />
  <img src="https://i.imgur.com/MJfu4uF.png" alt="Mist_Result" width="300" height="200"/>
</div>
<div style="display: flex;">
  <img src="https://i.imgur.com/6WBoTdm.png" alt="Sunny_Result" width="300" height="200" style="margin-right: 20px;" />
  <img src="https://i.imgur.com/u490Jg9.png" alt="Cloudy_Result" width="300" height="200"/>
</div>





<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Future Work -->
## Future Work
<br>- Weekly weather updates
<br>- Pictures for Clothing Recoomendations
<br>- More data about weather(High and Low, Average, etc.)
<br>- More backgroud audios and images for more weather conditions


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Alexis Guzman - [Linkedin](https://www.linkedin.com/in/alexis-guzman-cs9/) - aleguzmancs9@gmail.com
<br>Dalia Cabrera - [Linkedin](https://www.linkedin.com/in/dalia-c-4754a4247/) - daliaesmcabrera@outlook.com
<br>Jean-Luc Martel - [Linkedin](https://www.linkedin.com/in/jean-luc-martel-csumb/) - jmartel@gmail.com
<br>Ahmed Torki [Linkedin](https://www.linkedin.com/in/torki-ah/) - torki.ah.dev@gmail.com


Project Link: [https://github.com/aleguzmancs9/Weather.git](https://github.com/aleguzmancs9/Weather)




<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: linkedin.com/in/alexis-guzman-cs9
[OpenAI-url]: https://openai.com/
[Python-url]: https://www.python.org/
[WeatherAPI-url]: https://www.weatherapi.com/
[IpstackAPI-url]: https://ipstack.com/
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[JavaScript-url]: https://www.javascript.com/
