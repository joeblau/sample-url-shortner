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
import simplejson as json

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('JJB Short!')

class ShortenURLHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Shorten URL')
  def post(self):
    # Parse Inputs {long_url:..., custom_short_code(optional): ...} 
    data = None
    try: 
      data = json.loads(self.request.body)
    except Exception, error:
      self.response.write(error)
    # Check Data 
    
    # Generate Response  {success: true/false, short_code}
    self.response.write(data)
    
class CustomShortCodeHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Custom Short Code')
  def post(self):   
    self.response.write('Custom Short Code')

class NotFoundPageHandler(webapp2.RequestHandler):
  def head(self):
    self.get()
    self.response.clear()
  def get(self):
    self.error(404)
    self.response.write('404')
  def post(self):
    self.error(404)
    self.response.write('404')    

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/shorten_url', ShortenURLHandler),
  ('/*', CustomShortCodeHandler),
  ('/*', NotFoundPageHandler)
], debug=True)
