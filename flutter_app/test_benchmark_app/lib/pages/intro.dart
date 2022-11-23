import 'dart:async';

import 'package:flutter/material.dart';

import 'dashboard.dart';

class introduction extends StatefulWidget {
  const introduction({Key? key}) : super(key: key);

  static const String page_id = "Introduction";

  @override
  State<introduction> createState() => _introductionState();
}

class _introductionState extends State<introduction> {

  @override
  void initState() {
    Timer(const Duration(seconds: 2), () {
      Navigator.push(context, MaterialPageRoute(
          builder: (context) => dashBoard()));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return const Center(
        child: Text("Benchmark DashBodar",
          style: TextStyle(
            fontFamily: 'bold', color: Colors.black, fontSize: 40,),)
    );
  }
}
