import 'package:flutter/material.dart';
import 'package:just_audio/just_audio.dart';
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Audio Player',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late final AudioPlayer player;

  @override
  void initState() {
    super.initState();
    player = AudioPlayer();
  }

  @override
  void dispose() {
    player.dispose();
    super.dispose();
  }

  Future<void> play() async {
    await player.setUrl("http://192.168.43.188:5000/get_audio");
    player.play();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'ThirdEYE',
          style: TextStyle(
            fontSize: 24,
            color: Colors.blue,
            fontWeight: FontWeight.bold,
            fontStyle: FontStyle.italic,
            fontFamily: 'Roboto',
            letterSpacing: 1.2,
            wordSpacing: 2.0,
            decoration: TextDecoration.underline,
          ),
        ),
      ),
      body: Stack(
        children: [
          // Background image
          Positioned.fill(
            child: Image.asset(
              'assets/eye.jpg', // Path to your image asset
              fit: BoxFit.fill, // Cover the entire screen
            ),
          ),
          // Centered content
          Center(
            child: ElevatedButton(
              onPressed: play,
              child: Text('Play Audio'),
            ),
          ),
        ],
      ),
    );
  }
}