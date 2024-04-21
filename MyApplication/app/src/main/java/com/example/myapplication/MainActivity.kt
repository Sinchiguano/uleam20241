package com.example.myapplication

import android.content.Intent
import android.graphics.Bitmap
import android.os.Bundle
import android.provider.MediaStore
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import androidx.navigation.ui.setupActionBarWithNavController
import android.view.Menu
import android.view.MenuItem
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import com.example.myapplication.databinding.ActivityMainBinding
import com.example.myapplication.ml.MobilenetV110224Quant
import org.tensorflow.lite.DataType
import org.tensorflow.lite.support.image.ImageProcessor
import org.tensorflow.lite.support.image.TensorImage
import org.tensorflow.lite.support.image.ops.ResizeOp
import org.tensorflow.lite.support.image.ops.ResizeOp.ResizeMethod
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer

class MainActivity : AppCompatActivity() {

    lateinit var selectBtn:Button
    lateinit var predictBtn:Button
    lateinit var imageView:ImageView
    lateinit var resView:TextView
    lateinit var bitmap: Bitmap



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        selectBtn=findViewById(R.id.selectBtn)
        predictBtn=findViewById(R.id.predictBtn)
        imageView=findViewById(R.id.imageView)
        resView=findViewById(R.id.resView)



        var labels=application.assets.open("labels.txt").bufferedReader().readLines()
        //
        var imageProcessor=ImageProcessor.Builder()
            .add(ResizeOp(224, 224,ResizeOp.ResizeMethod.BILINEAR))
            .build()



        selectBtn.setOnClickListener{
            var intent =Intent()
            intent.setAction(Intent.ACTION_GET_CONTENT)
            intent.setType("image/*")
            startActivityForResult(intent, 100)

        }


        predictBtn.setOnClickListener {

            var tensorImage= TensorImage(DataType.UINT8)
            tensorImage.load(bitmap)
            tensorImage=imageProcessor.process(tensorImage)

            val model = MobilenetV110224Quant.newInstance(this)

            // Creates inputs for reference.
            val inputFeature0 = TensorBuffer.createFixedSize(intArrayOf(1, 224, 224, 3), DataType.UINT8)
            inputFeature0.loadBuffer(tensorImage.buffer)

            // Runs model inference and gets result.
            val outputs = model.process(inputFeature0)
            val outputFeature0 = outputs.outputFeature0AsTensorBuffer.floatArray
            var maxIdx=0
            outputFeature0.forEachIndexed {index,fl ->
                if(outputFeature0[maxIdx]<fl)
                {
                    maxIdx=index
                }
            }
            resView.setText(labels[maxIdx])
            // Releases model resources if no longer used.
            model.close()
        }



    }

//
//    private fun startActivitiesForResult(intent: Intent, i: Int) {
//
//    }


    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode==100){
            var uri=data?.data;
            bitmap=MediaStore.Images.Media.getBitmap(this.contentResolver,uri)
            imageView.setImageBitmap(bitmap)
        }









    }





}