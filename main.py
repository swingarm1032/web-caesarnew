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
        rotLabel = "<label>Rotate by:</label>"
        rotationInput = "<input type='number' name= 'rotation'/>"
        messaageLabel = "<label>Type a message:</label>"
        textArea = "<textarea name='message'></textarea>"
        submitButton = "<input type='submit'/>"
        form = ("<form method='post'>"
                + rotLabel + rotationInput + "<br>"
                + messaageLabel + textArea + "<br>"
                + submitButton + "</form>")
        header = '<h1>Web Caesar</h1>'
        self.response.write(header + form)

    def post(self):
        message = self.request.get("message")
        rot  = int(self.request.get('rotation'))
        encryptedMessage = caesar.encrypt(message, rot)
        self.response.write('The encrypted message is: ' + encryptedMessage)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
