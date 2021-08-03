class Messages:
    ADDED_TO_QUEUE = (
        "Your Request Has Been Added To The Queue. If You Have More Than {per_user_process_count} "
        "Ongoing Processes, Then This Process Will Only Start After One of Them Finishes"
    )
    MEDIA_MESSAGE_DELETED = "Don't Delete Messages"
    CANNOT_OPEN_FILE = "File Not Supported"
    PROCESS_TIMEOUT = (
        "Process Failed"
        "Taking Too Long To Complete It"
    )
    TRACK_USER_ACTIVITY = "User ID : `{chat_id}`"
    PROCESSING_REQUEST = "Processing...⏳"
    SCREENSHOT_AT = "ScreenShot At {time}"
    SCREENSHOT_PROCESS_FAILED = "Failed To Generate Screenshots"
    SCREENSHOT_PROCESS_SUCCESS = (
        " Screenshots Generated Successfuly \nRequested : {count}  "
        "Total : {total_count} "
        "\nUploading ⬆️"
    )
    PROCESS_UPLOAD_CONFIRM = (
        "Process Done In {total_process_duration}"
    )
    WRONG_FORMAT = "Please Follow The Format"
    VIDEO_PROCESS_CAPTION = "Sample video \n Duration : {duration}s \nFrom : {start}"
    SCREENSHOTS_START = "Generating Screenshot...⏳"

    SAMPLE_VIDEO_PROCESS_START = "Generating Sample Video...⏳"
    SAMPLE_VIDEO_PROCESS_FAILED = "Failed To Generate Sample Video"
    SAMPLE_VIDEO_PROCESS_SUCCESS = (
        "Sample Video Generated Successfuly"
    )

    SAMPLE_VIDEO_PROCESS_FAILED_GENERATION = (
        "Stream Link : {file_link}\n\n Duration {sample_duration} Sample Video"
        "Generation Failed\n\n{ffmpeg_output}"
    )
    SAMPLE_VIDEO_PROCESS_OPEN_ERROR = (
        "Stream Link : {file_link}\n\nSample Video Requested\n\n{duration}"
    )

    SCREENSHOTS_PROGRESS = "`{current}` Of `{total}` Generated"
    MANUAL_SCREENSHOTS_OPEN_ERROR = (
        "stream link : {file_link}\n\nRequested Manual Screenshots\n\n{duration}"
    )
    MANUAL_SCREENSHOTS_NO_VALID_POSITIONS = (
        "None Of The Given positions Where Valid"
    )
    MANUAL_SCREENSHOTS_VALID_PISITIONS_ABOVE_LIMIT = (
        "Only 10 Screenshots Can Be Generated, Found : `{valid_positions_count}`"
        "Valid Positions In Your Request"
    )
    MANUAL_SCREENSHOTS_INVALID_POSITIONS_ALERT = (
        "Found : `{invalid_positions_count}` Invalid Positions ({invalid_positions}).\n"
        "Generating Screenshots After Ignoring These"
    )
    MANUAL_SCREENSHOTS_FAILED_GENERATION = (
        "Stream Link : {file_link}\nManual Screenshots `{raw_user_input}`"
    )

    TRIM_VIDEO_INVALID_RANGE = "The Range Is Invalid"
    TRIM_VIDEO_DURATION_ERROR = (
        "Provide Any Range UpTo `{max_duration}s`"
        "Your Requested Range **{start} : {end}** Is `{request_duration}s` Long"
    )
    TRIM_VIDEO_OPEN_ERROR = "Stream Link : {file_link}\nTrim Video Requested\n{start} : {end}\n\n Duration : `{duration}`"
    TRIM_VIDEO_RANGE_OUT_OF_VIDEO_DURATION = (
        "The Requested Range Is Out Of The Videos Duration"
    )
    TRIM_VIDEO_PROCESS_FAILED = (
        "Failed To Trim The Video"
    )
    TRIM_VIDEO_PROCESS_FAILED_GENERATION = "Stream Link : {file_link}\n\nVideo Trim Failed.\n{start} : {end}\n\n{ffmpeg_output}"
    TRIM_VIDEO_PROCESS_SUCCESS = (
        "Video Trimmed Successfuly \nUploading ⬆️"
    )
    TRIM_VIDEO_START = "Trimming...⏳"

    SCREENSHOTS_OPEN_ERROR = "Stream Link : {file_link}\n\nRequested Screenshots : {num_screenshots}.\nDuration : {duration}"
    SCREENSHOTS_FAILED_GENERATION = (
        "Stream Link : {file_link}\n\n{num_screenshots} Screenshots Where Requested "
        "And Screenshots Where Not Generated"
    )

    SETTINGS = "Settings :"

    MEDIAINFO_START = "Generating Media Information...⏳"
