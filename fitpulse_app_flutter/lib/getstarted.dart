import 'package:flutter/material.dart';

class GetStartedPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: [
          // Background image for a fitness-themed design
          Image.asset(
            'assets/fitness.webp',
            fit: BoxFit.cover,
          ),
          // This is for better text visibility
          Container(
            color: Colors.black.withOpacity(0.6),
          ),
          // Main content layout
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 56.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // App title
                Text(
                  'FITPULSE APP',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 36),
                // FitPulse_app description
                Text(
                  'Your Personalized Body Fat\nPercentage Predictor.\nAchieve your fitness goals with\naccurate insights!',
                  style: TextStyle(
                    color: const Color.fromARGB(255, 206, 203, 203),
                    fontSize: 16,
                  ),
                ),
                SizedBox(height: 290),
                // "Get Started" button
                Center(
                  child: ElevatedButton(
                    onPressed: () {
                      // Navigate to the input field screen
                      Navigator.pushNamed(context, '/inputfield');
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Color(0xFFBC7731), // Button color
                      padding: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30),
                      ),
                    ),
                    child: Text(
                      'Get Started',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
