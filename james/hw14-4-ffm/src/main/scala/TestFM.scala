import com.github.fommil.netlib.BLAS._
import com.github.fommil.netlib.BLAS.{getInstance => blas}

import scala.util.Random

import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.evaluation.RegressionMetrics
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.regression._
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.mllib.evaluation.BinaryClassificationMetrics


object TestFM extends App {

  /**
    * print log loss and AUC for a model and dataset
    * model: trained FMM model
    * data: RDD containing training/validation/test data
    * desc: string used as title of dataset
    */
  def getMetrics(model: FMModel, 
                 data: RDD[LabeledPoint],
                 desc: String): Unit = {

    val dataSize = data.count()
    val preds = data.map { point =>
      val prediction = model.predict(point.features)
      (prediction, point.label)
    }

    val logLoss = preds.map { pred_label =>
      computeLogLoss(pred_label._1, pred_label._2)
      }.sum() / dataSize
    
    val metrics = new BinaryClassificationMetrics(preds)
    val auROC = metrics.areaUnderROC

    println(desc + " log loss = " + logLoss)
    println("Area under ROC = " + auROC)
  }

  /**
    * function to compute log loss
    * p: model probability for given data point
    * y: label for data point
    */
  def computeLogLoss(p: Double, y: Double): Double = {
    val epsilon = 10E-12
    var x = math.max(epsilon, p)
    x = math.min(1 - epsilon, p)
    val logLoss = y*math.log(x) + (1-y)*math.log(1-x)
    return -logLoss
  }

  override def main(args: Array[String]): Unit = {

    val sc = new SparkContext(new SparkConf().setAppName("TESTFM"))

    // process args. args 0-3 specify data locations. rest are hyperparams
    val train_in = args(0)
    val val_in = args(1)
    val test_in = args(2)
    val step_size = args(3).toDouble
    val reg = args(4).toDouble
    val num_iter = args(5).toInt

    // read in data
    val training = MLUtils.loadLibSVMFile(sc, train_in).cache()
    val validate = MLUtils.loadLibSVMFile(sc, val_in).cache()
    val test = MLUtils.loadLibSVMFile(sc, test_in).cache()

    // train model
    val fm1 = FMWithSGD.train(training, task = 1, numIterations = num_iter, stepSize = step_size, miniBatchFraction = 1.0, dim = (true, true, 4), regParam = (reg, reg, reg), initStd = 0.1)
    
    // get metrics against training, validation, and test sets
    getMetrics(fm1, training, "training")
    getMetrics(fm1, validate, "validation")
    getMetrics(fm1, test, "test")
  }
}
