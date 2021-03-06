from gram import Plot
read('data5.py')
gp = Plot()
gp.baseName = 'lineAndBar_better'
c = gp.bars(binNames,binVals)
c.barSets[0].fillColor = 'black!10'
gp.minBarValToShow = 0.0
gp.barNameAxis.title = None
gp.barValAxis.title = 'frequency'
gp.barNameAxis.barLabelsEvery = 2

gp.line(xx1, yy1, smooth=True)
gp.xAxis.position = 't'
gp.yAxis.position = 'r'
gp.xAxis.title = None
gp.xAxis.tickLabelsEvery = 2
gp.yAxis.title = 'density'
gp.png()
gp.svg() # line plot is not smooth
