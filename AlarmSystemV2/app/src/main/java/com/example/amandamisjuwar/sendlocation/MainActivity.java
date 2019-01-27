package com.example.amandamisjuwar.sendlocation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.app.PendingIntent;
import android.support.v4.app.ActivityCompat;
import android.Manifest;
import android.content.pm.PackageManager;
import android.volley.Request.Method;
import android.volley.RequestQueue;
import android.volley.Response;
import android.volley.VolleyError;
import android.volley.toolbox.StringRequest;
import java.util.Timer;
import java.util.TimerTask;


public class MainActivity extends AppCompatActivity  {
    private static final int MY_PERMISSIONS_REQUEST_SEND_SMS = 1;
<<<<<<< HEAD:AlarmSystemV2/app/src/main/java/com/example/amandamisjuwar/sendlocation/MainActivity.java

    Timer timer=null;
    int time=0;
    int sensor=0;
    double startTime;
    double endTime;
    boolean draw=false;

    // Instantiate the RequestQueue.
    RequestQueue queue = Volley.newRequestQueue(this);
    String url ="http://www.google.com";

    // Request a string response from the provided URL.
    StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
            new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    // Display the first 500 characters of the response string.
                    mTextView.setText("Response is: "+ response.substring(0,500));
                }
            }, new Response.ErrorListener() {
        @Override
        public void onErrorResponse(VolleyError error) {
            mTextView.setText("That didn't work!");
        }
    });

// Add the request to the RequestQueue.
queue.add(stringRequest);



=======
    
>>>>>>> 2bc639b9dd44f2493c9d212fcf2c264d1e009400:Send SMS (App v2)/app/src/main/java/com/example/amandamisjuwar/sendlocation/MainActivity.java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        checkForSmsPermission();
    }

    public void sendSms(View view) {
        // hardcoding the number we need to send emergency text to
        String phoneNumber = "2266066008";
        // making the text that is sent
        String message = "ALERT! CARGO THIEF DETECTED";
        // Use SmsManager.
        SmsManager smsManager = SmsManager.getDefault();
        String scAddress = null;
        PendingIntent sentIntent = null;
        PendingIntent deliveryIntent = null;
        smsManager.sendTextMessage
                (phoneNumber, scAddress, message,
                        sentIntent, deliveryIntent);
    }

    private void checkForSmsPermission() {
        if (ActivityCompat.checkSelfPermission(this,
                Manifest.permission.SEND_SMS) !=
                PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.SEND_SMS},
                    MY_PERMISSIONS_REQUEST_SEND_SMS);
        }
    }

}
