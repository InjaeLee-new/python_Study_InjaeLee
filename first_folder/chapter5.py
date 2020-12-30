import cx_Oracle 
class Oracle(object):
    
 def connect(self, username, password, hostname, port, servicename):        
  """ Connect to the database. """         
  try:            
   self.db = cx_Oracle.connect(username, password                                
    , hostname + ':' + port + '/' + servicename)  
    
  except cx_Oracle.DatabaseError as e:            
   error, = e.args            
   if error.code == 1017:                
    print('Please check your credentials.')            
   else:                
    print('Database connection error: %s'.format(e))   
    
   # Very important part!            
    raise         
   # If the database connection succeeded create the cursor        
   # we-re going to use.        
   self.cursor = db.Cursor()    
   
  def disconnect(self):        
   """        
   데이터 베이스 연결에 실패한다면, 대체할 수 있는 수단들이 있다.        
   """         
   try:            
    self.cursor.close()            
    self.db.close()        
   except cx_Oracle.DatabaseError:            
    pass     
    
  def execute(self, sql, bindvars=None, commit=False):               
    try:            
      self.cursor.execute(sql, bindvars)        
    except cx_Oracle.DatabaseError as e:            
      error, = e.args            
    if error.code == 955:                
      print('테이블이 이미 존재합니다.')            
    elif error.code == 1031:                
      print("미확인 에러 발생")         
      print(error.code)            
      print(error.message)            
      print(error.context)             
    
   # Raise the exception.            
  raise         
   # Only commit if it-s necessary.        
    if commit: 
      self.db.commit()