package ctf.crypto

import okhttp3.*
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.RequestBody.Companion.asRequestBody
import okhttp3.RequestBody.Companion.toRequestBody
import okhttp3.internal.closeQuietly
import java.io.File
import java.lang.Exception
import java.util.concurrent.TimeUnit

object NetUtils {
    fun post(url: String, params: HashMap<String, String>): String {
        try {
            val client = OkHttpClient.Builder()
                .connectTimeout(5, TimeUnit.SECONDS)
                .writeTimeout(5, TimeUnit.SECONDS)
                .readTimeout(10, TimeUnit.SECONDS)
                .build()
            val builder = FormBody.Builder()
            for (item in params) {
                builder.add(item.key, item.value)
            }

            val body = builder.build()
            val request = Request.Builder().url(url).post(body).build()
            val response = client.newCall(request).execute()
            if (response.isSuccessful) {
                val result = response.body?.string()
                response.closeQuietly()
                return result?:""
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return ""
    }


    fun get(url: String): String {
        try {
            val client = OkHttpClient.Builder().connectTimeout(5, TimeUnit.SECONDS)
                .readTimeout(10, TimeUnit.SECONDS).build()
            val request = Request.Builder().url(url).build()
            val response = client.newCall(request).execute()
            if (response.isSuccessful) {
                val result = response.body?.string()
                response.closeQuietly()
                return result?:""
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }

        return ""
    }

    fun postMultipleForm(url: String, map: Map<String, String>, files: ArrayList<File>, name: String): String {
        try {
            val client = OkHttpClient.Builder().connectTimeout(5, TimeUnit.SECONDS).readTimeout(5, TimeUnit.SECONDS)
                .writeTimeout(30, TimeUnit.SECONDS).build()
            val requestBody = MultipartBody.Builder().setType(MultipartBody.FORM)

            for (file in files) {
                val body = file.asRequestBody("image/*".toMediaTypeOrNull())
                requestBody.addFormDataPart(name, file.name, body)
            }

            for (item in map) {
                val body = item.value.toRequestBody("multipart/form-data; charset=utf-8".toMediaTypeOrNull())
                requestBody.setType(MultipartBody.FORM).addFormDataPart(item.key, null, body)
            }

            val request = Request.Builder().url(url).post(requestBody.build()).build()
            val response = client.newCall(request).execute()
            if (response.isSuccessful) {
                val result = response.body?.string()
                response.closeQuietly()
                return result?:""
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }

        return ""
    }



    private const val TAG = "NetUtils"
}
