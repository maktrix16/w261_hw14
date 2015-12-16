import com.github.fommil.netlib.BLAS._
import com.github.fommil.netlib.BLAS.{getInstance => blas}

import scala.util.Random

import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.evaluation.RegressionMetrics
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.regression._
import org.apache.spark.mllib.util.MLUtils


/**
 * Created by zrf on 4/18/15.
 */


object TestFM extends App {

  def computeLogLoss(p: Double, y: Double): Double = {
    val epsilon = 10E-12
    if(y == -1){
      if(p == 1){
        return -math.log(1 - p + epsilon)
      }else{
        return -math.log(1 - p)
      }
    }else{
      if(p == 0){
        return -math.log(epsilon + p)
      }else{
        return -math.log(p)
      }
    }
  }

  override def main(args: Array[String]): Unit = {

    val sc = new SparkContext(new SparkConf().setAppName("TESTFM"))

    val training = MLUtils.loadLibSVMFile(sc, "s3n://<access_key>:<secret_key>", false, -1, 20).cache()

    //    val task = args(1).toInt
    //    val numIterations = args(2).toInt
    //    val stepSize = args(3).toDouble
    //    val miniBatchFraction = args(4).toDouble

    val dataSize = training.count()

    val fm1 = FMWithSGD.train(training, task = 1, numIterations = 100, stepSize = 0.15, miniBatchFraction = 1.0, dim = (true, true, 4), regParam = (0, 0, 0), initStd = 0.1)

    val preds_fm1 = training.map { point =>
      val prediction = fm1.predict(point.features)
      (prediction, point.label)
    }
    
    val logLoss_fm1 = preds_fm1.map { pred_label =>
      computeLogLoss(pred_label._1, pred_label._2)
    }.sum() / dataSize

    println("training log loss for fm1 = " + logLoss_fm1)

    val fm2 = FMWithLBFGS.train(training, task = 1, numIterations = 20, numCorrections = 5, dim = (true, true, 4), regParam = (0, 0, 0), initStd = 0.1)

    val preds_fm2 = training.map { point =>
      val prediction = fm1.predict(point.features)
      (prediction, point.label)
    }
    
    val logLoss_fm2 = preds_fm1.map { pred_label =>
      computeLogLoss(pred_label._1, pred_label._2)
    }.sum() / dataSize

    println("training log loss for fm2 = " + logLoss_fm2)
    
  }
}
