import 'package:flutter/material.dart';
import 'package:test_benchmark_app/pages/dashboard.dart';
import 'package:test_benchmark_app/pages/intro.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'benchmark_dashboard',
      theme: ThemeData(
        primarySwatch: Colors.lightBlue,
      ),
      home: const introduction(),
      routes: {
        dashBoard.page_id : (context) => const dashBoard()
      },
    );
  }
}
