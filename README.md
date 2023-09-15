# BEANS: Property Chart Plotter

![LOGO](https://user-images.githubusercontent.com/48959790/194729624-0b88c702-fdd5-4826-a078-6df04f94309d.png)

Welcome to the BEANS: Property Chart Plotter.

Property Chart Plotter is a graph constructor to generate property charts (or Ashby charts/plots) from an input dataset. It allows convenient and effective comparison and selection of items, for example, materials, based on two properties. Such a plot is widely applied not only for materials science but in general for situations where things need to be selected based on numerical values. The explanation of this plotter will assume the user case of plotting materials property charts.


## Features
Built upon the theory of materials selection developed by Mike Ashby, this plotter has the following highlights:
1. Generation of property charts with material bubbles, family bubbles, lables and selection lines
2. Selecting and editing imported material data
3. Easy regrouping of materials into new families
4. Customizable axes with syntax input
5. Switching between log and linear scale
6. Percise color control of materials and family bubbles
7. Percise font and color control of labels
8. Full controll of the aspect ratio of the plot
9. Fully support the .csv data format previously prepared for CES softwares
10. User-friendly design of UI and UX

## Example
Refer the screenshot for its current UI and the plot style.
![image](https://user-images.githubusercontent.com/47532644/194804256-0ef97358-acb1-473a-b2ed-c51220c19794.png)

## Instructions
If you're familiar with python, you could clone the git project and run the tool on your platform.

If you don't like to worry about the programming language, the team is also publishing ready-to-use packages for Windows and Mac at important releases. The release packages can be found [here](https://github.com/TOBgit/MaterialPlot/tags). The latest release with the binary package is v0.2.1.

### Prompt in Chat-GPT4 to extract and tabulate data for this tool.
Prompt example:
extract the material name, and its properties (modulus, and yield strength) into a table from the following text, segmenting the mean and the error of the value into different columns, for example,  property_mean; covert values of different units to one unit:  Stainless steel has a modulus of 310 ± 10 GPa and yield strength of 15 ± 1 GPa. The modulus of Copper is 150 ± 5 MPa and yield strength of it is 0.03 GPa. In terms of glass, the modulus is 200 MPa but there is no yield strength.
Result example:
| Material       | Modulus_mean (GPa) | Modulus_error (GPa) | Yield_strength_mean (GPa) | Yield_strength_error (GPa) |
|-----------------|--------------------|---------------------|---------------------------|-----------------------------|
| Stainless steel | 310                | 10                  | 15                        | 1                           |
| Copper          | 0.150              | 0.005               | 0.03                      | 0                           |
| Glass           | 0.200              | 0                   | NaN                       | NaN                         |


## Fun fact behind the scene

The lead developers of this tool are friends from high school. They used to play together in World of Warcarft, leading a guild named 'Times of Beans'. The property chart, with its materials bubbles like beans and family bubble-like pods, is unexpectedly reminiscent. While it is unknown if the guild is still alive, the developers are more than happy to work together on one project again. By the way, the developers were playing Mage, Rogue, Warlock, and Warrior. There is no healer on the team. So when they are out for a wild task like this, they can only survive by eating and drinking the mage bread/water provided by the kind Mage :(

If you would enjoy this tool, you can [tip](https://www.paypal.com/donate/?business=UTH9TVWVJE93G&no_recurring=1&item_name=Support+the+TOB+team+to+move+on.&currency_code=USD) us some Savory Deviate Delight (it's a famous dish in World of Warcarft in case you don't know what it is). The team will appreciate your support and keep up the good work.

## References
### Theory behind this tool:

Ashby (1992) Materials Selection in Mechanical Design

### Journal articles using these plots:
Wesgt et al. (2015) Bioinspired structural materials, Nature Materials

### Cite this tool:
Lao, Weimin, Yin, Kaiyang, Li, Tienan, & Huang, Han. (2022). BEANS: Property Chart Plotter (v0.2.1). Zenodo. https://doi.org/10.5281/zenodo.7182691

You can export it to your reference management software through: https://zenodo.org/record/7182691

