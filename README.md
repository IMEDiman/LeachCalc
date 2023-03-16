# LEACHABILITY
<div style="text-align: justify"> The leachability concept which is implemented in this tool represents an advanced way to estimate mobility. Leachability is defined as the predicted potential of a chemical to leach through an unsaturated soil profile of 1 m thickness under worst-case pedo-climatic boundary conditions [1]. Adsorption to soil (Koc) combined with degradation in the soil matrix (DegT50 according to [2]) were considered as the main drivers for the transport of substances through soil. Based on the percentage of the substance leached to a soil depth of 1 m as a f unction of the substance amount at the soil surface the following metric for mobility is proposed

|Percentage   | Mobility|
|---|---|
|< 1 % | not mobile|
|1 % - 10 %| mobile|
|> 10 %|very mobile

The leaching is calculated with the freely available FOCUS-PELMO 6.6.4 [3] for a set of 41 DT50 by 21 KOC combinations (861 combinations). This is done for the 9 locations defined in the FOCUS framework [1,4] for a simulated time of 120 years. For each location the 80th percentile of annual percentage leached mass at a depth of 100 cm is calculated and the average over all locations is taken. The table containing the resulting leaching percentages is stored in lookup_table.txt and can be obtained via pressing the button "Copy Lookup Table to Clipboard".
If a combination of input parameters is not represented in the lookup table an interpolation is performed. This is done with the RectBivariateSpline function from the python3 module scipy.interpolate [5].

[1] FOCUS (2000) “FOCUS groundwater scenarios in the EU review of active substances” Report of the FOCUS Groundwater  cenarios Workgroup, [EC Document Reference Sanco/321/2000 rev.2, 202pp](https://esdac.jrc.ec.europa.eu/public_path/projects_data/focus/gw/doc.html).

[2] European Food Safety Authority, 2014. EFSA Guidance Document for evaluating laboratory and field dissipation studies to obtain DegT50 values of active substances of plant protection products and transformation products of these active substances in soil. [EFSA Journal 2014;12(5):3662, 37 pp., doi:10.2903/j.efsa.2014.3662](https://www.efsa.europa.eu/en/efsajournal/pub/3662)

[3] Klein M., Thomas K., Trapp M., Guerniche D. (2016), [publication](https://www.umweltbundesamt.de/publikationen/protection-of-the-groundwater-against-loads-of-0), [Download](https://esdac.jrc.ec.europa.eu/projects/pelmo)

[4] European Commission (2014) “Assessing Potential for Movement of Active Substances and their Metabolites to Ground Water in the EU” Report of the FOCUS Ground Water Work Group, [EC Document Reference Sanco/13144/2010 version 3, 613 pp](https://www.researchgate.net/publication/270393285_Assessing_potential_for_movement_of_active_substances_and_their_metabolites_to_ground_water_in_the_EU_The_final_report_of_the_Groundwater_work_group_of_FOCUS).

[5] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, CJ Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E.A. Quintero, Charles R Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. [Nature Methods, 17(3), 261-272](https://www.nature.com/articles/s41592-019-0686-2). 

# INSTALL AND RUN
Clone the repository to some place on your local device with [git](https://git-scm.com/download/win) (v2.37). The program was tested on OS Windows but the python code may also work on Linux distributions. 
Open cmd/terminal

    git clone https://github.com/IMEDiman/LeachCalc.git

You need an installation of [python3](https://www.python.org/downloads/) (v3.10).
To run leachCalc.py you will need to have the python packages installed which are listed in requirements.txt.
The easiest way to do this is with pip (v22.3) (download [`get-pip.py`](https://bootstrap.pypa.io/get-pip.py) and install with `python3 get-pip.py`):


    cd LeachCalc
    pip install -r requirements.txt

## leachCalc.py

leachCalc.py opens a graphical user interface. You can run leachCalc.py with

    python3 leachCalc.py

Another possiblity for Windows users is to [download](software.ime.fraunhofer.de/https://software.ime.fraunhofer.de/Leaching_Calculator/) a standalone executable which does not need any python installations.

## leachCalc_CLI.py
leachCalc_CLI.py is a command line interface. Substance parameters can be passed as arguments such as

    python3 leachCalc_CLI.py <substance_name> <koc> <DegT50>

As above, another possiblity for Windows users is to [download](software.ime.fraunhofer.de/https://software.ime.fraunhofer.de/Leaching_Calculator/) a standalone executable which does not need any python installations.


# USAGE

## leachCalc
The substance name and the corresponding set of values for Koc and DegT50 need to be entered into the appropriate input fields. Alternatively, the up- and down arrows can be used. A condensed result is output in the text field box which is updated whenever the input parameters are changed. The result can be copied with the "Copy to Clipboard"-button and pasted into any text editor of choice. 
Based on the lookup-table and the interpolation method a contour plot is created representing the three mobility classes as function of Koc and DT50. The mobility class of the respective substance is maked with a cross which is updated whenever the input changes.The figure can be saved as a PNG, JPG or PDF file with the "Save Figure"-button.

# BUG REPORTS

For reporting bugs, asking questions, giving remarks and suggestions, we welcome you to use the issue tracker: https://github.com/IMEDiman/LeachCalc/issues

# CONTACT

Dimitrios Skodras - dimitrios.skodras@ime.fraunhofer.de

Project link: https://github.com/IMEDiman/LeachCalc

# CREDITS

The author thanks Michael Klein, Judith Klein and Bernhard Jene for support and fruitful discussions. This project was financed by CropLife Europe in B-1040 Brussels, BELGIUM

# LICENCE

This project is licensed under GNU General Public License. A version of it should be shipped with this file. If not, you can find the text [here](https://www.gnu.org/licenses/gpl-3.0.en.html).
