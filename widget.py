from mosaico import widget
import datetime

fontName = "10x20"
timeHeight = 10
dateHeight = 35

# Create text for day
dayText = widget.createText()
dayText.setFont(fontName)
dayText.moveTo(8, timeHeight)  

# Create text for slash
slashText = widget.createText()
slashText.setFont(fontName)
slashText.moveTo(27, timeHeight)  
slashText.setHexColor("#ff0000")

# Create text for month
monthText = widget.createText()
monthText.setFont(fontName)
monthText.moveTo(36, timeHeight)  

# Create text for hours
hourText = widget.createText()
hourText.setFont(fontName)
hourText.moveTo(8, dateHeight)  

# Create text for colon
colonText = widget.createText()
colonText.setFont(fontName)
colonText.moveTo(26, dateHeight) 

# Create text for minutes
minuteText = widget.createText()
minuteText.setFont(fontName)
minuteText.moveTo(35, dateHeight)  

# Variable to keep track of the colon visibility state
colon_visible = True

def loop():
  global colon_visible
  
  current_time = datetime.datetime.now()
  monthText.setText(current_time.strftime("%m"))
  dayText.setText(current_time.strftime("%d"))
  hourText.setText(current_time.strftime("%H"))
  minuteText.setText(current_time.strftime("%M"))
  slashText.setText("/")
  
  # Toggle the colon visibility
  if colon_visible:
    colonText.setText(":")
  else:
    colonText.setText("")
  
  # Update colon visibility state
  colon_visible = not colon_visible