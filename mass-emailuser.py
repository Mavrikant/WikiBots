# -*- coding: utf-8 -*-
# !/usr/bin/python

import mavri

subject= "Email Subject"

text ="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam lobortis ornare finibus. Suspendisse sed vehicula orci, eget aliquet lorem. Integer lobortis magna venenatis mi pellentesque, nec aliquam tellus ultricies. Etiam lacinia urna sit amet nulla pharetra dapibus. Phasellus venenatis nibh ac nulla tempus, eu malesuada mauris rhoncus. Morbi sit amet varius diam, id dapibus arcu. Pellentesque in ullamcorper dolor, placerat faucibus massa. Integer tortor lorem, gravida elementum nunc sit amet, vestibulum ultricies nibh. Fusce viverra vehicula velit vitae efficitur. Praesent eget felis imperdiet, auctor est vitae, viverra mi. Nullam auctor est nibh, eu congue sem commodo et.

Nunc vitae finibus nisl, a vehicula ante. Quisque lorem augue, viverra sit amet ex id, auctor consectetur turpis. Vivamus tempor elit quis purus pellentesque vehicula. Curabitur faucibus semper nisl ac luctus. Fusce consectetur justo in consequat lacinia. Etiam nec felis vestibulum, elementum erat et, imperdiet magna. Nunc arcu nisi, imperdiet sit amet pharetra id, rutrum vitae odio. Nam ex enim, varius ac elementum et, placerat sit amet odio. Quisque vitae nisl at ante elementum tincidunt.

Donec ac ligula odio. Vivamus sed nisi facilisis, porta mauris nec, porta turpis. Nulla tempus eget lacus eget molestie. Pellentesque luctus laoreet libero, nec faucibus nunc bibendum quis. Pellentesque in sapien cursus, bibendum leo et, varius justo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam at nunc non neque vulputate lacinia. Nunc eget interdum diam. Nunc at tincidunt urna.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris eget erat sed nibh sagittis auctor. Fusce lectus nunc, convallis non dolor eu, faucibus volutpat tellus. Etiam vehicula malesuada porta. Pellentesque vehicula neque id eros hendrerit dapibus. Nam sit amet metus tortor. Sed vel malesuada nunc, a blandit mi. Cras et metus eleifend, aliquam nisi at, pulvinar eros. Integer fringilla fringilla nunc sed finibus. Proin convallis finibus diam, nec hendrerit ante congue et. Fusce vel sem nisi. Nullam nec orci in lectus tempor feugiat sit amet vel dui. Ut ac feugiat tortor. Morbi laoreet quis arcu et tempor. Praesent a nisi orci. Nulla auctor arcu sit amet ligula tempus consequat.

Etiam rhoncus arcu ac metus tincidunt scelerisque. Nam tincidunt dui elit, vitae egestas dui mattis nec. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam sollicitudin magna ex, vitae egestas tellus consequat id. Nulla mollis, purus non blandit laoreet, risus enim finibus quam, vel aliquet arcu ligula sit amet arcu. Praesent rhoncus nibh feugiat nisl sollicitudin sagittis. Aenean a orci est.

"""


users= ['Mavrikant', 'Mavrikant2', 'Mavrikant Bot']

xx = mavri.login('tr.wikipedia', 'Mavrikant')
print xx.text
for user in users:
    print mavri.emailuser('tr.wikipedia', user, subject, text, xx).text


