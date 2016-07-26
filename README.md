# WeatherPredictionAlgorithm

<b>Assumptions & Generalizations</b><br/> 
First things first, weather prediction requires a lot of data. So we would need a lot of basic weather monitoring devices scattered every 100-200km. A device that measures the five pillars of weather – Minimum Temperature, Maximum Temperature, Humidity, Rainfall and mean Pressure. Since what happens in the oceans are of high importance as well, we need to cover a sizeable portion of it too. Alternatively, this may be possible using satellites.
Also, weather – unless too extreme – does not change drastically. Almost all changes follow a smooth progression. Furthermore, weather more or less also has a cyclic nature to it. Hence historical data would be very helpful.

<b>Logic</b><br/>
If I need to predict what the weather at a point A would be tomorrow, I would collect the below info:
<ol>
<li>Five weather parameters at point A for the last 7 days. This would give an idea of the current trend.</li>
<li>Five weather parameters at points within 200 or so km for the last 7 days. This is especially important in case of weather dependencies like with pressure & temperature differences that create thunderstorm and heavy winds.</li>
<li>Five weather parameters at point A for previous year in the same time period. The time period would be 7 days before and after the current day – that is 14 days’ data from last year with the required date as the center. This is to infer from the cyclic nature of weather.</li>
</ol>
Assuming that the prediction is required for 20th July 2016, we will fetch data for 13th July 2016 to 19th July 2016 – let’s call it <b>Set 0</b>. This will give the existing trend. 
<br/><br/>Next will take data from 13th July 2015 to 27th July 2015 for historical reference. We will split the second set of data – 14 days data – into multiple sets of 7 consecutive days. That is 13th July 2015 to 19th July 2015 will be <b>Set 1</b>; 14th July 2015 to 20th July 2015 will be <b>Set 2</b> etc. Thus we will get 7 sets of data.
<br/><br/>We then have to compare the current week’s set, <b>Set 0</b>, to these new sets of data <b>Set 1</b>, <b>Set 2</b> etc till <b>Set 7</b>. There are various statistical methods to compare similarity and diversity of sample sets – for instance Jaccard Index. We would compare the Jaccard Distance for each set with Set 0 and find the most similar one. From this, we can get to know what happened last year when situations similar to the current ones were prevailing. Assume that <b>Set 3</b> had the most similar data.
<br/><br/>Now we need to plot all this data for each of the weather parameters. Plot the trend of minimum temperature from Set 0 – i.e. previous seven days. On the same graph, plot the data from Set 3 and Set 4 to see what had happened in the past. <b>This would make Part One</b><br/><br/>
<b>Part Two</b> would have to deal with weather at nearby points. For instance, climatologists already have models for what combination of weather parameters contribute to high winds or thunderstorm. So again we need to compare the weather parameters for Point A with the weather parameters at nearby points. This would give indications if weather at nearby points are going to affect the model predicted at Part One.<br/><br/>
Comparing both these parts, we can arrive at a fairly reliable, pattern oriented, weather prediction.
