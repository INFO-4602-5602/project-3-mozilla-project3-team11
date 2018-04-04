<h2> Project 2: </h2>

<h2> Description of Visualizations </h2>

<h3> Visualization #1: </h3>

This interactive stacked bar chart describes people's fear and excitement levels with resepect to their self-described technical skill level. The different colors in each stack represent the different answers to the questions regarding their excitement or fears, which are indicated in the legend. Specifically these questions were as follows:

--Thinking about a future in which so much of your world is connected to the internet leaves you feeling: Super excited, On the fence, A little wary, Cautiously optimistic, Scared as hell.

--What are you most excited about as we move toward a digitally connected future?

For both questions, we see that a majority of the respondents identified as Average User or Technically Savvy. 

For the first question, among the Average User or Technically Savvy categories, the majority were 'Cautiously optimisitic' and 'A little wary'. Among the Ultra Nerds, most were 'Cautiously optimistic' and none of the Luddites were 'Super excited' and most were 'Cautiously optimistic'. 

For the second question, most of Ultra Nerds and Technically Savvy individuals were most excited about 'How easy it would make life'. Among the Average Users and Luddites most of them didn't agree with any of the displayed any of the options listed. This might indicate a general low level of excitement when it comes to technology, given how they identified their own skill levels.

<p>Corresponding folder: vis1 </p>

<h3> Visualization #2: </h3>



<p>Corresponding folder: vis2 </p>


<h3> Visualization #3: </h3>

This visualization is a coordinated view of an interactive pie chart and bar chart. The pie chart shows the distrbution of languages spoken by the respondants. Upon clicking on a wedge of the pie chart, a bar chart appears showing the number of respondents that speak the selected language who understood various technology concepts.

Across all languages, the most understood concept was 'Connected Devices', followed by 'VPN'. We thought it might be interested to investigate whether there were any terms that were highly understood or misunderstood for specific languages; however, this is not what we see. We would likely see more drastic changes in the bar chart if we were to switch between users of different self-described technological skill level rather than language.

<p>Corresponding folder: vis3 </p>

<h2> Design Process: </h2>

We brainstormed and prototyped using whiteboard and marker to get a sense of how our visualizations should look. In addition, we analyzed the documents provided by Mozilla which gave us a sense of the data distributions as well as the questions they were interested in exploring, as stakeholders. We then came up with a list of five potential prototypes that we could convert to visualizations in code. Once the final set of three were selected, we decided to code it up in JavaScript, specifically using D3, since we decided that it would be most conducive to the features we wanted from the visualizations.

<h2> Team Roles: </h2>

Adam was responsible for the data processing and creation of visualization 1. Shantanu was responsible for data processing and creation of visualization 2. Andrew was responsible for data processing and creation of visualization 3. Shruthi and Emily were responsible for design and selection of the three vizualizations to work on. Shruthi and Emily also compiled the README.

<h3> How to Run the Project: </h3>

<h5> Requirements: </h5>

Web Browser, preferably Chrome or Firefox. 

Python >= 2.7

<h5> Command to Run Code <h5>

Set up a python server using one of the following two commands based on the python version installed on your computer:
# If Python version is 3.X
python -m http.server
# If Python version is 2.X
python -m SimpleHTTPServer

In your web browser, access localhost:8000. Navigate to the folder corresponding to the visualization you would like to see (vis1, vis2, or vis3) and click on the .html file.

