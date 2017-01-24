import bs4 as bs

html = '''
<div class="form-question-body">
   <div class="input">
      <ul>
         <li>Napoleonic Wars DLC</li>
      </ul>
   </div>
</div>


<div class="form-question-body">
   <div class="input-data">
      No
   </div>
</div>

<div class="form-question-body">
   <div class="input-data">
      I wish to play a more structured form of game play than standard vanilla and to become part of a community. I have played a sizable amount of hours with friends. I am easy to get along with and good at following orders from being an eagle scout. I am a decent shot in most shooter games and have extensively studied older styles of warfare including Napoleonic warefare.
   </div>
</div>

<div class="form-question-body">
   <div>Value: 17</div>
</div>

<div class="form-question-body">
   <div class="input">
      <ul>
         <li>North America</li>
      </ul>
   </div>
</div>

<div class="form-question-body">
   <div class="input">
      <ul>
         <li>Yes.</li>
      </ul>
   </div>
</div>

<div class="form-question-body">
   <div class="input">
      <ul>
         <li>Yes Sir!</li>
      </ul>
   </div>
</div>





<div class="form-question-body">
   <div class="input">
      <div class="chk-item">

         <div class="chk">
            <input name="appform[825j2isyfo][Monday Training 8pm EST]" onclick="return false;" type="checkbox" value="Monday Training 8pm EST"/>
         </div>
         <div class="chk-label">
            Monday Training 8pm EST
         </div>
         <div class="clearing">
            <!-- -->
         </div>

      </div>

      <div class="chk-item">
         <div class="chk">
            <input name="appform[825j2isyfo][Tuesday Conquest 8pm EST]" onclick="return false;" type="checkbox" value="Tuesday Conquest 8pm EST"/>
         </div>
         <div class="chk-label">
            Tuesday Conquest 8pm EST
         </div>
         <div class="clearing">
            <!-- -->
         </div>
      </div>

      <div class="chk-item">
         <div class="chk">
            <input checked="checked" name="appform[825j2isyfo][Thursday Training 8pm EST]" onclick="return false;" type="checkbox" value="Thursday Training 8pm EST"/>
         </div>
         <div class="chk-label">
            Thursday Training 8pm EST
         </div>
         <div class="clearing">
            <!-- -->
         </div>
      </div>

      <div class="chk-item">
         <div class="chk">
            <input checked="checked" name="appform[825j2isyfo][Friday Linebattle 8pm EST]" onclick="return false;" type="checkbox" value="Friday Linebattle 8pm EST"/>
         </div>
         <div class="chk-label">
            Friday Linebattle 8pm EST
         </div>
         <div class="clearing">
            <!-- -->
         </div>
      </div>

      <div class="chk-item">
         <div class="chk">
            <input checked="checked" name="appform[825j2isyfo][Saturday Linebattle 8pm EST]" onclick="return false;" type="checkbox" value="Saturday Linebattle 8pm EST"/>
         </div>
         <div class="chk-label">
            Saturday Linebattle 8pm EST
         </div>
         <div class="clearing">
            <!-- -->
         </div>
      </div>

      <div class="chk-item">
         <div class="chk">
            <input checked="checked" name="appform[825j2isyfo][Sunday Linebattle/Promotions 8pm EST]" onclick="return false;" type="checkbox" value="Sunday Linebattle/Promotions 8pm EST"/>
         </div>
         <div class="chk-label">
            Sunday Linebattle/Promotions 8pm EST
         </div>
         <div class="clearing">
            <!-- -->
         </div>
      </div>
   </div>
</div>

<div class="form-question-body">
   <div class="input">
      <ul>
         <li>63e Member</li>
      </ul>
   </div>
</div>

<div class="form-question-body">
   <div class="input-data">
      InfamousCavelord
   </div>
</div>

<div class="form-question-body">
   <div class="input">
      <ul>
         <li>Yes</li>
      </ul>
   </div>
</div>



<div class="form-question-body">
   <div class="input-data">
      https://steamcommunity.com/profiles/76561198055070225
   </div>
</div>

<div class="app_header_user_details">
   <a class="element_username" href="/profile/1097523" target="_blank">slammer128</a>
   <div class="app_header_user_ip">
      IP: 74.5.134.103
   </div>
</div>



<div class="app_header_user_meta">
   <div class="app_header_user_site">63ème Régiment</div>
   <div class="app_header_user_status">
      <a class="app_header_user_avatar_mini" data-minitooltip="Jordan" data-minitooltip-userid="10812534" href="http://63eregiment.enjin.com/profile/10812534" target="_blank"><img height="16" onerror="this.src='http://enjin.host/profile/images/avatar/tiny.png';" src="http://assets-cloud.enjin.com/users/10812534/avatar/tiny.1460662069.png" width="16"/></a> <a class="element_username" href="/profile/10812534" target="_blank">Jordan</a> <span class="app_header_user_date">
      on						Jan 14, 17					</span>
      <span class="approved">APPROVED</span>
   </div>
</div>

'''
html2 = '''
'[\'\\n\', <a class="element_username" href="/profile/17719555" target="_blank">Zachman81503</a>, \' \', <div class="app_header_user_ip">\n                    IP: 66.42.240.223
</div>, \'\\n\', \'\\n\', <div class="input">\n<ul>\n<li>Napoleonic Wars DLC</li>\n</ul>\n</div>, \' \', \'\\n\', <div class="input-data">\nno</div>, \'\\n\', \'\\n\', <div class="input-data">\ni was invited by  Mandacek. i do have alot of experience with NW. I love mount and blade NW<br/>\nI am 13 and i made a friend named  Mandacek. he is very nice. sorry the answers were out of order.</div>, \'\\n\', \'\\n\', <div>Value: 13</div>, \' \', \'\\n\', <div class="input">\n<ul>\n<li>North America</li>\n</ul>\n</div>, \' \', \'\\n\', <div class="input">\n<ul>\n<li>Yes.</li>\n</ul>\n</div>, \' \', \'\\n\', <div class="input">\n<ul>\n<li>Yes Sir!</li>\n</ul>\n</div>, \' \', \'\\n\', <div class="input">\n<div class="chk-item">\n<div class="chk">\n<input checked="checked" name="appform[825j2isyfo][Monday Training 8pm EST]" onclick="return false;" type="checkbox" value="Monday Training 8pm EST"/>\n</div>\n<div class="chk-label">\n\t\t\tMonday Training 8pm EST\t\t</div>\n<div class="clearing"><!-- --></div>\n</div>\n<div class="chk-item">\n<div class="chk">\n<input name="appform[825j2isyfo][Tuesday Conquest 8pm EST]" onclick="return false;" type="checkbox" value="Tuesday Conquest 8pm EST"/>\n</div>\n<div class="chk-label">\n\t\t\tTuesday Conquest 8pm EST\t\t</div>\n<div class="clearing"><!-- --></div>\n</div>\n<div class="chk-item">\n<div class="chk">\n<input checked="checked" name="appform[825j2isyfo][Thursday Training 8pm EST]" onclick="return false;" type="checkbox" value="Thursday Training 8pm EST"/>\n</div>\n<div class="chk-label">\n\t\t\tThursday Training 8pm EST\t\t</div>\n<div class="clearing"><!-- --></div>\n</div>\n<div class="chk-item">\n<div class="chk">\n<input name="appform[825j2isyfo][Friday Linebattle 8pm EST]" onclick="return false;" type="checkbox" value="Friday Linebattle 8pm EST"/>\n</div>\n<div class="chk-label">\n\t\t\tFriday Linebattle 8pm EST\t\t</div>\n<div class="clearing"><!-- --></div>\n</div>\n<div class="chk-item">\n<div class="chk">\n<input name="appform[825j2isyfo][Saturday Linebattle 8pm EST]" onclick="return false;" type="checkbox" value="Saturday Linebattle 8pm EST"/>\n</div>\n<div class="chk-label">\n\t\t\tSaturday Linebattle 8pm EST\t\t</div>\n<div class="clearing"><!-- --></div>\n</div>\n<div class="chk-item">\n<div class="chk">\n<input name="appform[825j2isyfo][Sunday Linebattle/Promotions 8pm EST]" onclick="return false;" type="checkbox" value="Sunday Linebattle/Promotions 8pm EST"/>\n</div>\n<div class="chk-label">\n\t\t\tSunday Linebattle/Promotions 8pm EST\t\t</div>\n<div class="clearing"><!-- --></div>\n</div>\n</div>, \'\\n\', \'\\n\', <div class="input">\n<ul>\n<li>63e Member</li>\n</ul>\n</div>, \' \', \'\\n\', <div class="input-data">\nMandacek</div>, \'\\n\', \'\\n\', <div class="input">\n<ul>\n<li>Yes</li>\n</ul>\n</div>, \' \', \'\\n\', <div class="input-data">\nhttp://steamcommunity.com/profiles/76561198312612795/</div>, \'\\n\', \'\\n\', <div class="app_header_user_site">63ème Régiment</div>, \'\\n\', <div class="app_header_user_status">\n<span class="approved">OPEN</span>\n</div>, \'\\n\']' '''

soup = bs.BeautifulSoup(html2, 'lxml')
#all other info fuckery

guy=[]
for form in soup.find_all("div",class_="form-question-body"):
    form = form.text.strip('\n').strip('  ').strip('%s\n')
    guy.append(form)

# pop the long useless col
for i in range(len(guy)):
    if '\n\n\n\n\n\n\n\n\n\n' in guy[i]:
        to_pop = i
try:
    guy.pop(to_pop)
except UnboundLocalError:
    pass




#attendnce fuckery
#next return the value only
attendance = []
for check in soup.find_all("div",class_="chk"):
    for box in check:
        if 'checked' in str(box):

            if 'Monday' in str(box):
                attendance.append('Monday')
            elif 'Tuesday' in str(box):
                attendance.append('Tuesday')
            elif 'Wednesday' in str(box):
                attendance.append('Wednesday')
            elif 'Thursday' in str(box):
                attendance.append('Thursday')
            elif 'Friday' in str(box):
                attendance.append('Friday')
            elif 'Saturday' in str(box):
                attendance.append('Saturday')
            elif 'Sunday' in str(box):
                attendance.append('Sunday')

            # print("TESTING ATT")
            # print(box)
            # attendance.append(box)
guy.append(attendance)


print (guy)
print('--------------')
for i in range(len(guy)):
    print(i)
    print (guy[i])
