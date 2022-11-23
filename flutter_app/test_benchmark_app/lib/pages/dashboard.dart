import 'dart:math';
import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;

TextStyle header() {
  return const TextStyle(fontSize: 20);
}

class dashBoard extends StatefulWidget {
  const dashBoard({Key? key}) : super(key: key);

  static const String page_id = "dashBoard";

  @override
  State<dashBoard> createState() => _dashBoardState();
}

class _dashBoardState extends State<dashBoard> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: const Icon(
          Icons.menu,
          color: Colors.white,
        ),
        centerTitle: false,
        backgroundColor: Colors.black,
        title: const Text(
          'DashBoard',
          style: TextStyle(color: Colors.white),
        ),
      ),
      backgroundColor: Colors.black,
      body: ListView(
        children: [
          _buildBody(),
          _buildBody(),
          _buildBody(),
          _buildBody(),
          _buildBody()
        ],
      ),
    );
  }

  Widget _buildBody() {
    return Padding(
      padding: const EdgeInsets.all(15.0),
      child: Column(
        children: [_buildCol()],
      ),
    );
  }

  Widget _buildCol() {
    double windowWidth = MediaQuery.of(context).size.width * 0.9;
    double windowHeight = MediaQuery.of(context).size.height;

    return Row(
      children: [
        STJODD(windowWidth: windowWidth, windowHeight: windowHeight),
        performPercent(windowWidth: windowWidth, windowHeight: windowHeight),
        barChartBlock(windowWidth: windowWidth, windowHeight: windowHeight),
        processPercent(windowWidth: windowWidth, windowHeight: windowHeight),
      ],
    );
  }
}

class processPercent extends StatelessWidget {
  const processPercent({
    Key? key,
    required this.windowWidth,
    required this.windowHeight,
  }) : super(key: key);

  final double windowWidth;
  final double windowHeight;

  @override
  Widget build(BuildContext context) {
    return Container(
        margin: const EdgeInsets.all(5.0),
        // padding: const EdgeInsets.all(5.0),
        width: windowWidth * 0.3,
        height: windowHeight * 0.3,
        // decoration: BoxDecoration(
        //     border: Border.all(
        //         color: Colors.black,
        //         width: 1
        //     ),
        //     borderRadius: BorderRadius.circular(10)
        // ),
        child: Row(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(0, 0, 5, 0),
              child: Container(
                width: windowWidth * 0.3 * 0.3,
                decoration: BoxDecoration(
                    color: const Color(0x499799AF),
                    // border: Border.all(
                    //     color: Colors.black,
                    //     width: 1
                    // ),
                    borderRadius: BorderRadius.circular(5)),
                child: Column(
                  children: [
                    const Text("A...",
                        style: TextStyle(fontSize: 15, color: Colors.white60)),
                    Container(
                      margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                      height: windowHeight * 0.3 * 0.25,
                      color: Colors.blueGrey,
                      child: const Center(
                        child: const Text(
                          "94%",
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ),
                      ),
                    ),
                    Container(
                      margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                      height: windowHeight * 0.3 * 0.25,
                      color: Colors.blueGrey,
                      child: const Center(
                        child: const Text(
                          "94%",
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ),
                      ),
                    ),
                    Container(
                      margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                      height: windowHeight * 0.3 * 0.25,
                      color: Colors.blueGrey,
                      child: const Center(
                        child: const Text(
                          "93%",
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(0, 0, 5, 0),
              child: Container(
                width: windowWidth * 0.3 * 0.3,
                decoration: BoxDecoration(
                    color: const Color(0x499799AF),
                    // border: Border.all(
                    //     color: Colors.black,
                    //     width: 1
                    // ),
                    borderRadius: BorderRadius.circular(5)),
                child: Column(
                  children: [
                    const Text("B...",
                        style: TextStyle(fontSize: 15, color: Colors.white60)),
                    Container(
                      margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                      height: windowHeight * 0.3 * 0.25,
                      color: Colors.lightGreen,
                      child: const Center(
                        child: const Text(
                          "71%",
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ),
                      ),
                    ),
                    Container(
                      margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                      height: windowHeight * 0.3 * 0.25,
                      color: Colors.blueGrey,
                      child: const Center(
                        child: const Text(
                          "86%",
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ),
                      ),
                    ),
                    Container(
                      margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                      height: windowHeight * 0.3 * 0.25,
                      color: Colors.blueGrey,
                      child: const Center(
                        child: const Text(
                          "87%",
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Container(
              width: windowWidth * 0.3 * 0.3,
              decoration: BoxDecoration(
                  color: const Color(0x499799AF),
                  // border: Border.all(
                  //     color: Colors.black,
                  //     width: 1
                  // ),
                  borderRadius: BorderRadius.circular(5)),
              child: Column(
                children: [
                  const Text("C...",
                      style: TextStyle(fontSize: 15, color: Colors.white60)),
                  Container(
                    margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                    height: windowHeight * 0.3 * 0.25,
                    color: Colors.lightGreen,
                    child: const Center(
                      child: const Text(
                        "88%",
                        style: TextStyle(
                            fontSize: 25,
                            fontWeight: FontWeight.bold,
                            color: Colors.white),
                      ),
                    ),
                  ),
                  Container(
                    margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                    height: windowHeight * 0.3 * 0.25,
                    color: Colors.lightGreen,
                    child: const Center(
                      child: const Text(
                        "86%",
                        style: TextStyle(
                            fontSize: 25,
                            fontWeight: FontWeight.bold,
                            color: Colors.white),
                      ),
                    ),
                  ),
                  Container(
                    margin: const EdgeInsets.fromLTRB(0, 5, 0, 0),
                    height: windowHeight * 0.3 * 0.25,
                    color: Colors.lightGreen,
                    child: const Center(
                      child: const Text(
                        "89%",
                        style: TextStyle(
                            fontSize: 25,
                            fontWeight: FontWeight.bold,
                            color: Colors.white),
                      ),
                    ),
                  ),
                ],
              ),
            )
          ],
        ));
  }
}

class barChartBlock extends StatelessWidget {
  const barChartBlock({
    Key? key,
    required this.windowWidth,
    required this.windowHeight,
  }) : super(key: key);

  final double windowWidth;
  final double windowHeight;

  @override
  Widget build(BuildContext context) {

    return Container(
      margin: const EdgeInsets.all(5.0),
      padding: const EdgeInsets.all(5.0),
      width: windowWidth * 0.5,
      height: windowHeight * 0.3,
      decoration: BoxDecoration(
          color: const Color(0x499799AF),
          // border: Border.all(
          //     color: Colors.black,
          //     width: 1
          // ),
          borderRadius: BorderRadius.circular(5)),
      child: StackedHorizontalBarChart.withSampleData(),
    );
  }
}

class performPercent extends StatelessWidget {
  const performPercent({
    Key? key,
    required this.windowWidth,
    required this.windowHeight,
  }) : super(key: key);

  final double windowWidth;
  final double windowHeight;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.all(5.0),
      padding: const EdgeInsets.all(5.0),
      width: windowWidth * 0.1,
      height: windowHeight * 0.3,
      decoration: BoxDecoration(
          color: const Color(0x499799AF),
          // border: Border.all(
          //     color: Colors.black,
          //     width: 1
          // ),
          borderRadius: BorderRadius.circular(5)),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          SizedBox(
            height: windowHeight * 0.3 * 0.05,
          ),
          Text(
            'Performance',
            style: TextStyle(fontSize: 10, color: Colors.white60),
          ),
          Text(
            "71%",
            style: TextStyle(
                fontSize: 25,
                fontWeight: FontWeight.bold,
                color: Colors.white60),
          ),
          SizedBox(
            height: windowHeight * 0.3 * 0.1,
          ),
          Text(
            'Availablity',
            style: TextStyle(fontSize: 10, color: Colors.white60),
          ),
          Text(
            "94%",
            style: TextStyle(
                fontSize: 25,
                fontWeight: FontWeight.bold,
                color: Colors.white60),
          ),
          SizedBox(
            height: windowHeight * 0.3 * 0.1,
          ),
          Text(
            'Quality',
            style: TextStyle(fontSize: 10, color: Colors.white60),
          ),
          Text(
            "88%",
            style: TextStyle(
                fontSize: 25,
                fontWeight: FontWeight.bold,
                color: Colors.white60),
          )
        ],
      ),
    );
  }
}

class STJODD extends StatelessWidget {
  const STJODD({
    Key? key,
    required this.windowWidth,
    required this.windowHeight,
  }) : super(key: key);

  final double windowWidth;
  final double windowHeight;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.all(5.0),
      padding: const EdgeInsets.all(5.0),
      width: windowWidth * 0.1,
      height: windowHeight * 0.3,
      decoration: BoxDecoration(
          // border: Border.all(
          //     color: Colors.black,
          //     width: 1
          // ),
          color: const Color(0x499799AF),
          borderRadius: BorderRadius.circular(5)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          SizedBox(
            height: windowHeight * 0.3 * 0.05,
          ),
          Text(
            'STJDAP \n ODD',
            style: TextStyle(fontSize: 15, color: Colors.white60),
          ),
          Center(
            heightFactor: 2.5,
            child: Text(
              "59%",
              style: TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                  color: Colors.white60),
            ),
          )
        ],
      ),
    );
  }
}

class StackedHorizontalBarChart extends StatelessWidget {
  final List<charts.Series<dynamic, String>> seriesList;
  final bool animate;

  StackedHorizontalBarChart(this.seriesList, {this.animate = false});

  /// Creates a stacked [BarChart] with sample data and no transition.
  factory StackedHorizontalBarChart.withSampleData() {
    return StackedHorizontalBarChart(
      _createSampleData(),
      // Disable animations for image tests.
      animate: false,
    );
  }

  // EXCLUDE_FROM_GALLERY_DOCS_START
  // This section is excluded from being copied to the gallery.
  // It is used for creating random series data to demonstrate animation in
  // the example app only.
  factory StackedHorizontalBarChart.withRandomData() {
    return StackedHorizontalBarChart(_createRandomData(), animate: true,);
  }

  /// Create random data.
  static List<charts.Series<OrdinalSales, String>> _createRandomData() {
    final random = Random();

    final desktopSalesData = [
      OrdinalSales('2014', random.nextInt(100)),
      OrdinalSales('2015', random.nextInt(100)),
      OrdinalSales('2016', random.nextInt(100)),
      OrdinalSales('2017', random.nextInt(100)),
    ];

    final tableSalesData = [
      OrdinalSales('2014', random.nextInt(100)),
      OrdinalSales('2015', random.nextInt(100)),
      OrdinalSales('2016', random.nextInt(100)),
      OrdinalSales('2017', random.nextInt(100)),
    ];

    final mobileSalesData = [
      OrdinalSales('2014', random.nextInt(100)),
      OrdinalSales('2015', random.nextInt(100)),
      OrdinalSales('2016', random.nextInt(100)),
      OrdinalSales('2017', random.nextInt(100)),
    ];

    return [
      charts.Series<OrdinalSales, String>(
        id: 'Desktop',
        domainFn: (OrdinalSales sales, _) => sales.year,
        measureFn: (OrdinalSales sales, _) => sales.sales,
        data: desktopSalesData,
      ),
      charts.Series<OrdinalSales, String>(
        id: 'Tablet',
        domainFn: (OrdinalSales sales, _) => sales.year,
        measureFn: (OrdinalSales sales, _) => sales.sales,
        data: tableSalesData,
      ),
      charts.Series<OrdinalSales, String>(
        id: 'Mobile',
        domainFn: (OrdinalSales sales, _) => sales.year,
        measureFn: (OrdinalSales sales, _) => sales.sales,
        data: mobileSalesData,
      ),
    ];
  }

  // EXCLUDE_FROM_GALLERY_DOCS_END

  @override
  Widget build(BuildContext context) {
    // For horizontal bar charts, set the [vertical] flag to false.
    return charts.BarChart(
      seriesList,
      animate: animate,
      barGroupingType: charts.BarGroupingType.stacked,
      vertical: false,
    );
  }

  /// Create series list with multiple series
  static List<charts.Series<OrdinalSales, String>> _createSampleData() {
    final desktopSalesData = [
      OrdinalSales('2014', 5),
      OrdinalSales('2015', 25),
      OrdinalSales('2016', 100),
      OrdinalSales('2017', 75),
    ];

    final tableSalesData = [
      OrdinalSales('2014', 25),
      OrdinalSales('2015', 50),
      OrdinalSales('2016', 10),
      OrdinalSales('2017', 20),
    ];

    final mobileSalesData = [
      OrdinalSales('2014', 10),
      OrdinalSales('2015', 15),
      OrdinalSales('2016', 50),
      OrdinalSales('2017', 45),
    ];

    return [
      charts.Series<OrdinalSales, String>(
        id: 'Desktop',
        domainFn: (OrdinalSales sales, _) => sales.year,
        measureFn: (OrdinalSales sales, _) => sales.sales,
        data: desktopSalesData,
      ),
      charts.Series<OrdinalSales, String>(
        id: 'Tablet',
        domainFn: (OrdinalSales sales, _) => sales.year,
        measureFn: (OrdinalSales sales, _) => sales.sales,
        data: tableSalesData,
      ),
      charts.Series<OrdinalSales, String>(
        id: 'Mobile',
        domainFn: (OrdinalSales sales, _) => sales.year,
        measureFn: (OrdinalSales sales, _) => sales.sales,
        data: mobileSalesData,
      ),
    ];
  }
}

/// Sample ordinal data type.
class OrdinalSales {
  final String year;
  final int sales;

  OrdinalSales(this.year, this.sales);
}
