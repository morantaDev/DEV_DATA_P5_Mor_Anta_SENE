// console.log(d3);

const DUMMY_DATA = [
    {id: 'd1', value: 10, region:'USA'},
    {id: 'd2', value: 11, region:'India'},
    {id: 'd3', value: 12, region:'China'},
    {id: 'd4', value: 6, region:'Germany'}
];
// d3.select('div')
//     .selectAll('p')
//     // .data([1, 2, 3]) //datas can be a json object or any type of data
//     .data(DUMMY_DATA)
//     .enter()    //for free missing elements
//     .append('p')   //append a missing paragraph
//     .text(dta => dta.region);

// const container = d3.select('div')
//     .classed('container', true)
//     .style('border', '1px solid red')

// const bars = container
//     .selectAll('.bar')
//     .data(DUMMY_DATA)
//     .enter()
//     .append('div')
//     .classed('bar', true)
//     .style('width','50px')
//     .style('height',data => (data.value * 15) + "px");


const xScale = d3.scaleBand().domain(DUMMY_DATA.map((dataPoint) => dataPoint.region)).rangeRound([0, 250]).padding(0.1);   //a function that allow to calculate positions the x axis
const yScale = d3.scaleLinear().domain([0, 15]).range([200, 0]); //function that transform a value to another number(scaleBand, scaleLinear)
const container = d3.select('#container')
    .classed('container', true)
    .style('border', '1px solid red')

const bars = container
    .selectAll('.bar')
    .data(DUMMY_DATA)
    .enter()
    .append('rect')
    .classed('bar', true)
    .attr('width',xScale.bandwidth())
    .attr('height',(data) => 200 - yScale(data.value))
    .attr('x', data => xScale(data.region))
    .attr('y', data => yScale(data.value));

// // Add text labels (regions) to the x-axis
// const xAxisLabels = container.append('g')
//     .attr('transform', `translate(0, ${200})`);

// xAxisLabels.selectAll('.x-axis-label')
//     .data(DUMMY_DATA)
//     .enter()
//     .append('text')
//     .classed('x-axis-label', true)
//     .text(data => data.region)
//     .attr('x', data => xScale(data.region) + xScale.bandwidth() / 2)
//     .attr('y', 15) // Adjust this value as needed to control the vertical position of the labels
//     .attr('text-anchor', 'middle')
//     .style('font-size', '12px');


// const xScale = d3.scaleBand().domain(DUMMY_DATA.map((dataPoint) => dataPoint.region)).rangeRound([0, 250]).padding(0.1);
// const yScale = d3.scaleLinear().domain([0, 15]).range([200, 0]);
// const container = d3.select('#container')
//     .classed('container', true)
//     .style('border', '1px solid red');

// const bars = container
//     .selectAll('.bar')
//     .data(DUMMY_DATA)
//     .enter()
//     .append('rect')
//     .classed('bar', true)
//     .attr('width', xScale.bandwidth())
//     .attr('height', (data) => 200 - yScale(data.value))
//     .attr('x', data => xScale(data.region))
//     .attr('y', data => yScale(data.value));

// // Add text labels (regions) to the x-axis
// const xAxisLabels = container.append('g')
//     .attr('transform', `translate(0, ${height})`); // Adjusted the y-coordinate for the labels

// xAxisLabels.selectAll('.x-axis-label')
//     .data(DUMMY_DATA)
//     .enter()
//     .append('text')
//     .classed('x-axis-label', true)
//     .text(data => data.region)
//     .attr('x', data => xScale(data.region) + xScale.bandwidth() / 2)
//     .attr('y', 15) // Adjust this value as needed to control the vertical position of the labels
//     .attr('text-anchor', 'middle')
//     .style('font-size', '12px');



// Sample data (renamed to listTenData)
const listTenData = [
    { label: "Category A", value: 30 },
    { label: "Category B", value: 20 },
    { label: "Category C", value: 50 },
  ];
  
// SVG dimensions and center
const width = 400;
const height = 400;
const centerX = width / 2;
const centerY = height / 2;

// Create the SVG container
const svg = d3.select("#chart")
  .attr("width", width)
  .attr("height", height);

// Create the pie generator
const pie = d3.pie()
  .value(d => d.value)
  .sort(null);

// Define the arc generator
const radius = Math.min(width, height) / 2 - 30; // Add padding from the edge
const arc = d3.arc()
  .innerRadius(0)
  .outerRadius(radius);

// Create the pie slices
const pieData = pie(listTenData);

// Create a group to center the chart
const chartGroup = svg.append("g")
  .attr("transform", `translate(${centerX}, ${centerY})`);

// Add the slices to the chart
chartGroup.selectAll("path")
  .data(pieData)
  .enter()
  .append("path")
  .attr("d", arc)
  .attr("fill", (d, i) => d3.schemeCategory10[i]);

// Add labels to the slices
const labelArc = d3.arc().innerRadius(radius * 0.7).outerRadius(radius * 0.7);
chartGroup.selectAll("text")
  .data(pieData)
  .enter()
  .append("text")
  .attr("transform", d => `translate(${labelArc.centroid(d)})`)
  .attr("dy", "0.35em")
  .text(d => d.data.label)
  .style("text-anchor", "middle")
  .style("fill", "white");