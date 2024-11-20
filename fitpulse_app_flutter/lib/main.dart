import 'package:flutter/material.dart';
import 'getstarted.dart';
import 'inputfield.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Body Fat Percentage Prediction', // This is the App title
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple), // App's primary color
        useMaterial3: true,
      ),
      // Setting up routes for different screens
      initialRoute: '/',  // Starting page of the app
      routes: {
        '/': (context) => GetStartedPage(), // Route for the welcome page
        '/inputfield': (context) => InputFieldPage(), // Route to input metrics page
      },
    );
  }
}
