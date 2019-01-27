package com.example.amandamisjuwar.sendlocation;


import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.app.PendingIntent;
import android.support.v4.app.ActivityCompat;
import android.Manifest;
import android.content.pm.PackageManager;



public class MainActivity extends AppCompatActivity  {

    private static final int MY_PERMISSIONS_REQUEST_SEND_SMS = 1;
  
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
        String message = "ALERT! CARGO THEFT DETECTED";
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
