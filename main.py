#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import logging
import os
from google.appengine.api import users
from google.appengine.ext import ndb
import json

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Quotes(ndb.Model):
    text = ndb.StringProperty()
    # text = ndb.StringProperty(repeated = True)
# poster = ndb.StringProperty(required = false);

class MainHandler(webapp2.RequestHandler):
    def get(self):
        quotes = {}
        list_of_quotes = Quotes.query();
        all_quotes = [];
        for quote in list_of_quotes:
            all_quotes.append(quote.text);
        quotes["results"] = all_quotes;

        template = jinja_environment.get_template('templates/homepage.html')
        self.response.write("this it totally the get page");
        self.response.write(template.render(quotes));
    def post(self):
        text = self.request.get('quote');
        quote = Quotes(text = text);
        quote.put();
        self.response.write("this it totally the post page");
        self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
