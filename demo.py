from us_visa.pipline.training_pipeline import TrainPipeline



from dotenv import load_dotenv
load_dotenv()
obj= TrainPipeline()
obj.run_pipeline()