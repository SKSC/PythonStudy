from selenium import webdriver;

registerurl="https://skillselect.gov.au/SKILLSELECT/ExpressionOfInterest/PreReg/Start"

def process():
    #initialize
    dr = webdriver.Firefox()
    
    #page 1 -- terms and conditions
    dr.find_element_by_xpath("//input[@type='checkbox']").click() #tick on the checkbox
    dr.find_element_by_xpath("//button[@name='Next']").click()  # click on next button
    
    #page 2 -- personal details
    fn = dr.find_element_by_xpath("//input[@id='EOI_PersonalDetails_FamilyName']")
    fn.send_keys('FamilyName') #find and set family name
    fn = dr.find_element_by_xpath("//input[@id='EOI_PersonalDetails_GivenNames']")
    fn.send_keys('Given Names') #find and set family name
    dr.find_element_by_xpath("//input[@name='EOI.PersonalDetails.Sex' and @value='M']").click() #select the sex
    dob = dr.find_element_by_xpath("//input[@id='EOI_PersonalDetails_DateOfBirth']")
    dob.send_keys("01/01/1988") #set date of birth
    cob = dr.find_element_by_xpath("//select[@id='EOI_PersonalDetails_CountryOfPassport']")
    cob.send_keys("CHINA") #set country of birth
    cop = dr.find_element_by_xpath("//select[@id='EOI_PersonalDetails_CountryOfPassport']")
    cop.send_keys("CHINA") #set country of birth
    #set the citizenship
    dr.find_element_by_xpath("//input[@name='EOI.PersonalDetails.IsCitizenOfPassportCountry' and @value='True']").click()
    #set the citizenship of another country
    dr.find_element_by_xpath("//input[@name='EOI.PersonalDetails.IsCitizenOfAnotherCountry' and @value='False']").click()
    #other passport
    dr.find_element_by_xpath("//input[@name='EOI.PersonalDetails.HasOtherPassports' and @value='False']").click()
    #usual country of residence
    ucr = dr.find_element_by_xpath("//select[@id='EOI_PersonalDetails_CountryOfResidence']")
    ucr.send_keys("AUSTRALIA")
    state = dr.find_element_by_xpath("//select[@id='EOI_PersonalDetails_State']")
    state.send_keys("Victoria")
    dr.find_element_by_xpath("//input[@id='EOI_PersonalDetails_Postcode']").send_keys('3163')
    #relationship status
    rs = dr.find_element_by_xpath("//select[@id='EOI_PersonalDetails_RelationshipStatus']")
    rs.send_keys('NEVER MARRIED')
    #press button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 3 -- confirm provided information
    #confirm information correct
    dr.find_element_by_xpath("//input[@name='EOI.PersonalDetails.IdentityConfirmed' and @value='True']").click()
    #click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 4 -- create account
    dr.find_element_by_xpath("//input[@id='UserVM_Password']").send_keys('Asdf11111') #set passport
    dr.find_element_by_xpath("//input[@id='UserVM_PasswordConfirmation']").send_keys('Asdf11111') #confirm passport
    dr.find_element_by_xpath("//input[@id='UserVM_Email']").send_keys('usermail@gmail.com') # set email
    dr.find_element_by_xpath("//input[@id='UserVM_EmailConfirmation']").send_keys('usermail@gmail.com') #confirm email
    #set preferred passport
    dr.find_element_by_xpath("//select[@id='UserVM_SecretAnswer1']").send_keys('Preferred Passport')
    #passport number
    dr.find_element_by_xpath("//input[@id='UserVM_SecretAnswer2']").send_keys('G30912345')
    #expire date
    dr.find_element_by_xpath("//input[@id='UserVM_SecretAnswer3']").send_keys('06/08/2024')
    #
    #Google chapture, do know how to do yet
    #
    #
    #click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 5 -- confirm account information
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 6 -- skillselect login
    #confirm the policy
    dr.find_element_by_xpath("//input[@id='chkIAccept']").click()
    #user name
    dr.find_element_by_xpath("//input[@name='txtUsername']").send_keys("username")
    #passport
    dr.find_element_by_xpath("//input[@name='txtPassword']").send_keys("Asdf11111")
    #click login button
    dr.find_element_by_xpath("//input[@name='Button1']").click()
    
    
    #page 7 -- EOI(3/12) -- Visa Type
    #visa type
    dr.find_element_by_xpath("//input[@name='VisaSubclassVM.HasSkilledIndependentVisa189']").click()
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 8 -- EOI(4/12) --Family Member
    #include family member or not
    dr.find_element_by_xpath("//input[@name='EOI.FamilyMembers.HasFamilyMembers' and @value='False']").click()
    #will include family member in the future or not
    dr.find_element_by_xpath("//input[@name='EOI.FamilyMembers.IsAccompaniedByPartner' and @value='False']").click()
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 9 EOI(5/12) -- English Language
    #undertake IELTE
    dr.find_element_by_xpath("//input[@name='EOI.ClientLanguage.HasUndertakenEnglishTest' and @value='True']").click()
    #IELTS
    dr.find_element_by_xpath("//input[@name='EOI.ClientLanguage.TestName' and @value='IELTS']").click()
    #IELTS Date
    dr.find_element_by_xpath("//input[@name='EOI.ClientLanguage.TestDate']").send_keys("09/09/2013")
    #IELTS Reference number
    dr.find_element_by_xpath("//input[@name='EOI.ClientLanguage.TestReferenceNumber']").send_keys("11AU305774FAMG240G")
    #listening score
    dr.find_element_by_xpath("//select[@name='EOI.ClientLanguage.ListeningScoreIELTS']").send_keys("7")
    #reading score
    dr.find_element_by_xpath("//select[@name='EOI.ClientLanguage.ReadingScoreIELTS']").send_keys("7")
    #Writing score
    dr.find_element_by_xpath("//select[@name='EOI.ClientLanguage.WrittenScoreIELTS']").send_keys("7")
    #Speaking score
    dr.find_element_by_xpath("//select[@name='EOI.ClientLanguage.SpeakingScoreIELTS']").send_keys("7")
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 10 EOI(6/12) -- Education
    #undertake IELTE
    dr.find_element_by_xpath("//input[@name='EOI.ClientEducation.HasPreviouslyStudied' and @value='True']").click()
    #Can add multiple education history
    #Add education history
    dr.find_element_by_xpath("//button[@name='AddEducationHistory']").click()
    #Qualification
    dr.find_element_by_xpath("//select[@name='EducationVM.AddEducationHistory.Qualification']").send_keys("Masters Degree in Science, Business or Technology")
    #course name
    dr.find_element_by_xpath("//input[@name='EducationVM.AddEducationHistory.CourseName']").send_keys("Master of Computer Science")
    #institution name
    dr.find_element_by_xpath("//input[@name='EducationVM.AddEducationHistory.InstitutionName']").send_keys("RMIT")
    #Country of Institution
    dr.find_element_by_xpath("//select[@name='EducationVM.AddEducationHistory.Country']").send_keys("Australia")
    #Institution campus
    dr.find_element_by_xpath("//input[@name='EducationVM.AddEducationHistory.Campus']").send_keys("City")
    #postcode of campus
    dr.find_element_by_xpath("//input[@name='EducationVM.AddEducationHistory.CampusPostCode']").send_keys("3000")
    #date from
    dr.find_element_by_xpath("//input[@name='EducationVM.AddEducationHistory.DateFrom']").send_keys("15/03/2011")
    #date to
    dr.find_element_by_xpath("//input[@name='EducationVM.AddEducationHistory.DateTo']").send_keys("15/03/2014")
    #confirm
    dr.find_element_by_xpath("//button[@name='InsertEducationHistory']").click()
    #
    #Can add multiple education history
    #Australian study requirement
    dr.find_element_by_xpath("//input[@name='EOI.ClientEducation.MeetStudyRequirements' and @value='True']").click()
    #regional Australia -- study
    dr.find_element_by_xpath("//input[@name='EOI.ClientEducation.HasStudiedRegional' and @value='True']").click()
    # Credentialled community language
    dr.find_element_by_xpath("//input[@name='EOI.ClientEducation.HasCommunityLanguageQualification' and @value='True']").click()
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    
    #page 11 EOI(7/12) -- Skills assessment
    #nominated occupation
    dr.find_element_by_xpath("//input[@name='EOI.ClientSkills.NominatedOccupation.ANZSCO']").send_keys("Developer Programmer - 261312")
    # has assessment from relevant authority
    dr.find_element_by_xpath("//input[@name='EOI.ClientSkills.HasSkillsAssessment' and @value='True']").click()
    # select the assessing authority
    dr.find_element_by_xpath("//select[@name='EOI.ClientSkills.AssessmentAuthority']").send_keys("Australian Computer Society")
    #assessment date
    dr.find_element_by_xpath("//input[@name='EOI.ClientSkills.AssessmentDate']").send_keys("05/06/2014")
    #assessment reference number
    dr.find_element_by_xpath("//input[@name='EOI.ClientSkills.ReferenceNumber']").send_keys("GXXXXXXXXX")
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    #page 12 EOI(8/12) -- Employment and Professional Year
    #Can add multiple education history
    #
    #
    #
    #Add employment history
    dr.find_element_by_xpath("//button[@name='AddEmploymentHistory']").click()
    #employment position
    ep = dr.find_element_by_xpath("//input[@name='EmploymentVM.AddEmploymentHistory.Position']")
    ep.send_keys("Development Manger")
    #employer name
    en = dr.find_element_by_xpath("//input[@name='EmploymentVM.AddEmploymentHistory.EmployerName']")
    en.send_keys("IDTC")
    #employer country
    ec = dr.find_element_by_xpath("//select[@name='EmploymentVM.AddEmploymentHistory.Country']")
    ec.send_keys("AUSTRALIA")
    #employer state
    es = dr.find_element_by_xpath("//select[@name='EmploymentVM.AddEmploymentHistory.State']")
    es.send_keys("Victoria")
    #related nominated occupation
    dr.find_element_by_xpath("//input[@name='EmploymentVM.AddEmploymentHistory.IsRelatedNominatedOccupation' and @value='True']").click()
    #starting date
    sd = dr.find_element_by_xpath("//input[@name='EmploymentVM.AddEmploymentHistory.DateFrom']")
    sd.send_keys("02/02/2011")
    #ending date
    ed = dr.find_element_by_xpath("//input[@name='EmploymentVM.AddEmploymentHistory.DateTo']")
    ed.send_keys("18/09/2014")
    #confirm 
    ed = dr.find_element_by_xpath("//button[@name='InsertEmploymentHistory']").click()
    #
    #
    #
    #professional year
    dr.find_element_by_xpath("//input[@name='EOI.ClientEmployment.HasCompletedProfessionYear' and @value='True']").click()
    #professional year field
    pyf = dr.find_element_by_xpath("//select[@name='EOI.ClientEmployment.CompletedProfessionalYear']")
    pyf.send_keys("Computer Science")
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    
    
    #page 13 EOI(9/12) Confirmation of Points
    #language
    dr.find_element_by_xpath("//input[@name='EOI.PointsConfirmation.LanguageAbilityConfirmed' and @value='True']").click()
    #education
    dr.find_element_by_xpath("//input[@name='EOI.PointsConfirmation.EducationHistoryConfirmed' and @value='True']").click()
    #study requirement
    dr.find_element_by_xpath("//input[@name='EOI.PointsConfirmation.MeetStudyRequirementConfirmed' and @value='True']").click()
    #regional Australia Study
    dr.find_element_by_xpath("//input[@name='EOI.PointsConfirmation.RegionalStudyConfirmed' and @value='True']").click()
    #Credentialled community language
    dr.find_element_by_xpath("//input[@name='EOI.PointsConfirmation.CommunityLanguageConfirmed' and @value='True']").click()
    #Employment
    dr.find_element_by_xpath("//input[@name='EOI.PointsConfirmation.EmploymentHistoryConfirmed' and @value='True']").click()
    #Professional Year
    dr.find_element_by_xpath("//input[@name='EOI.PointsConfirmation.ProfessionalYearConfirmed' and @value='True']").click()
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    
    
    #page 14 EOI(10/12) Declarations
    #read and understand
    dr.find_element_by_xpath("//input[@name='EOI.Declarations.HasReadAndUnderstood' and @value='True']").click()
    #complete correct
    dr.find_element_by_xpath("//input[@name='EOI.Declarations.HasCompleteCorrect' and @value='True']").click()
    #understand misleading
    dr.find_element_by_xpath("//input[@name='EOI.Declarations.HasUnderstoodMisleading' and @value='True']").click()
    #not visa
    dr.find_element_by_xpath("//input[@name='EOI.Declarations.HasUnderstoodNotVisa' and @value='True']").click()
    #update changes
    dr.find_element_by_xpath("//input[@name='EOI.Declarations.WillUpdateChanges' and @value='True']").click()
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    
    #page 15 EOI(11/12) Review Page
    #review confirm
    dr.find_element_by_xpath("//input[@name='EOI.ReviewConfirm' and @value='True']").click()
    #confirm and click Next button
    dr.find_element_by_xpath("//button[@name='Next']").click()
    
    
    #page 16 EOI(12/12) Visa type summary
    dr.find_element_by_xpath("//button[@name='Submit']").click()
    
    dr.quit()
    
def main():
    process()
    
    
main()
    
    
    