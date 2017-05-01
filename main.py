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
import caesar

class MainHandler(webapp2.RequestHandler):

    def get(self):
        message = 'Hello, World!!!!!!!!'
        rot = 13
        encryptedMessage = caesar.encrypt(message,rot)
        heading = "<h1>" + "Enter message to encrypt: "+ "</h1>"
        textArea = "<textarea>" + encryptedMessage + "</textarea>"
        submitButton = "<input type='submit'/>"
        form = "<form>" + textArea + "<br>" + submitButton + "</form>"
        self.response.write(heading + "<br>" + form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
