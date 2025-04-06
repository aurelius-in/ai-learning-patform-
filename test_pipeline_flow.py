def test_training_pipeline_flow():
    from src.pipelines.training_pipeline import run_training_pipeline
    try:
        run_training_pipeline()
        assert True  # If no exception, pipeline runs
    except Exception as e:
        assert False, f"Pipeline failed with error: {e}"

def test_inference_pipeline_flow():
    from src.pipelines.inference_pipeline import run_inference_pipeline
    try:
        run_inference_pipeline()
        assert True  # Should complete without error
    except Exception as e:
        assert False, f"Inference failed with error: {e}"