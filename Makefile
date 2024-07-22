install-deps:
	pip install -r api_gateway/app/requirements.txt \
		-r api_gateway/test_api_gateway/requirements.txt \
		-r file_service/app/requirements.txt \
		-r file_service/test_file_service/requirements.txt
