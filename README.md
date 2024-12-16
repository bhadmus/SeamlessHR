# SeamlessHR Assessment

---


## Table of Contents

---


- [Dependencies](#dependencies)
- [Guide](#guide)
- [Execution](#execution)
- [Contact](#contact)

## Dependencies

---
- [ ] [Python](https://www.python.org/downloads/)
- [ ] [Behave](https://pypi.org/project/behave/)
- [ ] [Selenium](https://pypi.org/project/selenium/)


## Guide

> [!INFO]
> 
> Have Python installed and for best practice install a virtual environment.
> 
> You can install virtualenv to create one for instance or whichever way you prefer.



- Clone the repository into a desired location
- Open the cloned repository
- Start the virtual environment
- Open a terminal in it and run `pip install -r requirements.txt`

## Execution

You can run all tests locally from your project root using:

```bash
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html
```
This would run the entire tests and also generate  a report. 

## Contact

For any questions or concerns please reach out to me via my [email](mailto:bhadmusademola.1@gmail.com)