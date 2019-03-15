# NCopyright Nicklas Tegner - @NicklasMCHD
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.

import braillecodec as braille

start = "Hello World 123"
print(f"Starting string: {start}")

encoder_result = braille.encode(start)
print(encoder_result)

decoder_result = braille.decode(encoder_result)
print(decoder_result)

print(f"Start equal to decoded_result: {start == decoder_result}")