# SBR for NCNU Linux管理與實務 指導：BlueT 
羞羞平衡車 Shyshy Balancing Robot

##概念發想
暨大是個美麗的校園，但幅員真的很廣大，有天在管院，看到有人在玩兩輪平衡車，站在上面利用身體重心移動。這對於想欣賞風景，又不想動腳的人真的相當方便，因此我們想利用他的原理，DIY一台用PI整合的兩輪平衡車。
[![參考影片](http://i.ytimg.com/vi/YRdBsVTHEG0/0.jpg)](https://www.youtube.com/watch?v=7-mgaIe287M)

##實作所需材料
<table>
	<thead>
		<tr>
			<td>材料名稱</td>
			<td>取得來源</td>
			<td>價格</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Raspberry Pi</td>
			<td>課程提供</td>
			<td>Free</td>
		</tr>
		<tr>
			<td>馬達控制板 L298N</td>
			<td>保保學長友情贊助</td>
			<td>Free</td>
		</tr>
		<tr>
			<td>陀螺儀 MPU-6050</td>
			<td>飆機器人</td>
			<td>$100</td>
		</tr>
		<tr>
			<td>碳刷馬達(紅頭) * 2</td>
			<td>保保學長友情贊助</td>
			<td>Free</td>
		</tr>
		<tr>
			<td>四驅車輪子 * 2</td>
			<td>保保學長友情贊助</td>
			<td>Free</td>
		</tr>
		<tr>
			<td>電池盒</td>
			<td>將為提供</td>
			<td>Free</td>
		</tr>
		<tr>
			<td>行動電源(供給PI電源)</td>
			<td>展瑩提供</td>
			<td>Free</td>
		</tr>
		<tr>
			<td>杜邦線(公 - 母) * 6</td>
			<td>Moli提供</td>
			<td rowspan="2">Free</td>
		</tr>
		<tr>
			<td>杜邦線(母 - 母) * 4</td>
			<td>Moli提供</td>
		</tr>
	</tbody>
</table>

##實作
<p>剛開始我們有的設備是Pi、wifi網卡、tty線。</p>

<p>因為我們做的是會行動的東西，所以勢必最後要擺脫tty線。我們發現有兩種方式可行: <br>
1. 運用wifi網卡ssh進去Pi，在裡面啟動主程式。<br>
2. 在Pi開機時自動啟動python程式。(可google"/etc/rc.local")</p>

<p>一開始我們選擇第一種，因為可以不需要外接螢幕，用自己的筆電也可以開發與測試，希望就這樣一直到期末。<br>
自動連接網路教學: <br>
http://inpega.blogspot.tw/2013/09/blog-post_15.html<br>
但後來只要我們去查一下資料，一段時間沒有理Pi，他就會睡著，然後我們就要再等他回過神來連網路，這會花很多時間。因此最後我們採用連接螢幕開發，實際測試時再把他設定為開機後執行。</p>

<p>
sensor運作上<br>
陀螺儀運作方式是每隔一段時間，就可以運算出目前傾斜的角度。<br>
控制馬達的方式是運用Pi腳位輸出的訊號來控制前進或後退。<br>
因此我們運用的方法是，當平衡車處在一個安全的角度範圍內，則不需要動作，當向前傾倒超過某個角度時，要向前推進，把身體拉直，反之向後倒也是這樣的方式，<br>
因此陀螺儀偵測速度不宜太慢，不然會自己倒下來。<br>
而馬達的執行時間如果太短(想做微調的話)，則車子會像是在發抖，並不會起到拉直身體的作用。時間太長又會讓車子衝過頭，導致倒向反方向。<br>
所以大部分的時間，以及困難點是在微調「傾斜角度範圍」、「指令執行時間(sleep time)」上。
</p>

##可能會遭遇到的嚴重問題
<p>跟插、拔線有關的動作，最好都在沒有通電的狀況下完成。<br>
尤其是跟馬達有關的更要注意。在Pi運作的過程中對線做動作，有可能馬達的電會流到Pi身上，而馬達通常要足夠的電力才推的動，那不一定是Pi能夠負荷的。<br>
我們一開始想做的是飛行器，那需要很大的電輸出，我們習慣性的在Pi還在運作時對線做了動作，導致Pi出了一些問題。<br>
希望我們的體驗，能夠對未來的同學有所幫助
</p>

##接線方式
1.陀螺儀配置<br>
基本上陀螺儀上已經很清楚寫好他每個針腳對應的位置。<br>
![陀螺儀](https://github.com/NCNU-OpenSource/PPQ/blob/master/images/mpu-6050.jpg)
2.控制板配置<br>
控制板是參考去年BT-7的配線方法<br>
![控制板](https://github.com/NCNU-OpenSource/PPQ/blob/master/images/motor.jpg)

##DEMO
![Shyshy Balancing Robot](https://github.com/NCNU-OpenSource/PPQ/blob/master/images/finish.jpg)
[![DEMO影片](http://i.ytimg.com/vi/Ki7mhFmQ6sM/0.jpg)](https://www.youtube.com/watch?v=Ki7mhFmQ6sM)
