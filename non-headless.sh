#!/usr/bin/env bash

export headless=0; behave -f behave_html_formatter:HTMLFormatter -o reports/report.html

