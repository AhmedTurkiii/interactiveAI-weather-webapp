
<a name="readme-top"></a>




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aleguzmancs9/Weather">
    
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
PLACEHOLDER


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Python][Python-url]
* [Together.ai][Together-url]
* [WeatherAPI][WeatherAPI-url]
* [Flask][Flask-url]
* HTML
* [Bootstrap][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
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

### Installation

1. Get a free API Key at [https://www.weatherapi.com](https://www.weatherapi.com)
1. Get a free API Key at [https://together.ai/apis](https://together.ai/apis)
2. Import packages
   ```sh
   import requests
   ```
   ```sh
   from datetime import datetime
   ```
   ```sh
   from flask import Flask, render_template, request
   ```
   ```sh
   from main import get_weather_data
   ```
3. Enter your API in `terminal`
   ```bash
   export TOGETHEI_API_KEY='Enter Your Api'
   ```
4. Enter your API in `Main.py`
   ```reflex
   together.api_key = "Enter Your Api"
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<div style="display: flex;">
  
</div>





<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Alexis Guzman - [Linkedin](https://www.linkedin.com/in/alexis-guzman-cs9/) - aleguzmancs9@gmail.com
<br>Dalia Cabrera - [Linkedin](https://www.linkedin.com/in/dalia-c-4754a4247/) - daliaesmcabrera@outlook.com
<br>Jean-Luc Martel - [Linkedin](https://www.linkedin.com/in/jean-luc-martel-csumb/) - jmartel@gmail.com


Project Link: [https://github.com/aleguzmancs9/Weather.git](https://github.com/aleguzmancs9/Weather)




<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: linkedin.com/in/alexis-guzman-cs9
[Together.ai]: https://images.squarespace-cdn.com/content/v1/6358bea282189a0adf57fe16/f0f7f485-91ef-47f6-b67c-305c10d73b59/together.ai+logo.png?format=1500w
[Together-url]: https://together.ai/
[Python-url]: https://www.python.org/
[WeatherAPI-url]: https://www.weatherapi.com/
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Bootstrap-url]: https://getbootstrap.com/
